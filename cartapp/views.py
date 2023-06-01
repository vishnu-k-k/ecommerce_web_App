from django.shortcuts import render,redirect
from shop . models import Product
from . models import cart,cartitem
from django.core.exceptions import ObjectDoesNotExist
def _cart_id(request):
    Cart=request.session.session_key
    if not Cart:
        Cart=request.session.create()
    return Cart
def add_cart(request,product_id,):
    product=Product.objects.get(id=product_id)
    try:
        Cart=cart.objects.get(cart_id=_cart_id(request))
    except  cart.DoseNotExist:
        Cart=cart.objects.create(
              cart_id=_cart_id(request)

        )
        Cart.save(),
    try:
        Cart_item=cartitem.objects.get(product=product,Cart=Cart)
        Cart_item.quantity +=1
        Cart_item.save()
    except    cartitem.DoseNotExist:
       Cart_item=cartitem.objects.create(

                product=product,
                quantity=1,
                Cart=Cart

       )
       Cart_item.save()
    return redirect('Cart:Cart_details')
def Cart_details(request,total=0,counter=0,Cart_item=None):
    try:
        Cart=cart.object.get(cart_id=_cart_id(request))
        Cart_item=cartitem.objects.filter(Cart=Cart,active=True)
        for Cart_item in Cart_item:
            total+=(Cart_item.product.price * Cart_item . quantity)
            counter += Cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(Cart_item=Cart_item,total=total,counter=counter))
