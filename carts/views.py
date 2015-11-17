from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from products.models import Product, Variation
from .models import Cart, CartItem
from decimal import Decimal

def view(request):
    try:
        the_id = request.session['cart_id'] 
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart": cart}
    else:
        empty_message = "Your Cart is Empty, please keep shopping."
        context = {"empty": True, "empty_message": empty_message}
    template = "carts/view.html"
    return render(request, template, context)

def update_cart(request, slug):
    request.session.set_expiry(120000)
 
    try:
        the_id = request.session['cart_id'] 
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    product_var = [] # product variation
    if request.method == "POST":
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
                product_var.append(v)
            except:
                pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
       print "yeah"

    # if update_qty and qty: # for item removal
    if qty:
        if int(qty) <= 0:
           cart_item.delete()
        else:
           if len(product_var) > 0:
               cart_item.variations.clear()
               for item in product_var:
                   cart_item.variations.add(item)
           cart_item.quantity = qty
           cart_item.save()

    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)

    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total
    
    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = Decimal(str(new_total))
    cart.save()

    return HttpResponseRedirect(reverse("cart"))
