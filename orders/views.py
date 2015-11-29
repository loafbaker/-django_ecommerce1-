import stripe

from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
from accounts.models import UserAddress
from accounts.forms import UserAddressForm
from carts.models import Cart
from .models import Order
from .utils import id_generator

try:
    stripe_pub = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret = settings.STRIPE_SECRET_KEY
except Exception, e:
    raise NotImplementedError(str(e))

stripe.api_key = stripe_secret

def orders(request):
    context = {}
    template = "orders/user.html"
    return render(request, template, context)

# require user login
@login_required
def checkout(request):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        # work on some error messages
        return HttpResponseRedirect(reverse("cart"))


    address_form = UserAddressForm()
    try:
        address_added = request.GET.get('address_added')
    except:
        address_added = None

    if address_added is None:
       address_form = UserAddressForm()   
    else:
       address_form = None

    current_addresses = UserAddress.objects.filter(user=request.user)
    billing_addresses = UserAddress.objects.get_billing_address(user=request.user)
    # assign an address
    # run credit card

    if request.method == "POST":
        try:
            user_stripe = request.user.userstripe.stripe_id
            customer = stripe.Customer.retrieve(user_stripe)
            print customer
        except:
            customer = None

        if customer is not None:
            token = request.POST['stripeToken']
            card = customer.sources.create(source=token)
            charge = stripe.Charge.create(
                amount=int(new_order.final_total * 100),
                currency="usd",
                source=card, # obtained with Stripe.js
                customer=customer,
                description="Charge for %s" % (request.user.username)
            )
            print card
            print charge
            if charge['captured']:
                print 'charged'

    if new_order.status == 'Finished':
        # cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))

    context = {
        'order': new_order,
        'address_form': address_form,
        'current_addresses': current_addresses,
        'billing_addresses': billing_addresses,
        'stripe_pub': stripe_pub
    }
    template = "orders/checkout.html"
    return render(request, template, context)
