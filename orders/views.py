from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
import time

# Create your views here.
from carts.models import Cart
from .models import Order

def checkout(request):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))


    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        # assign a user to the order
        new_order.order_id = str(time.time())
        new_order.save()

    # assign an address
    # run credit card
    if new_order.status == 'Finished':
        cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))

    context = {}
    template = "products/home.html"
    return render(request, template, context)
