import imp
from .models import Order, Product
import json


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_items': 0, 'get_cart_total': 0}

    if cart:
        for item in cart:
            product = Product.objects.get(id=item)
            total = product.price * cart[item]['quantity']

            order['get_cart_items'] += cart[item]['quantity']
            order['get_cart_total'] += total

            order_item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image': product.image
                },
                'quantity': cart[item]['quantity'],
                'get_item_total': total
            }

            items.append(order_item)
    
    return {'order': order, 'items': items}


def cartData(request):
    if request.user.is_authenticated:
        custmomer = request.user.customer
        order, created = Order.objects.get_or_create(customer=custmomer, complete=False)
        items = order.cartitem_set.all()

    else:
        cookieData = cookieCart(request)
        items = cookieData['items']
        order = cookieData['order']

    return {'order': order, 'items': items}