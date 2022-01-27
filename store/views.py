import imp
from django.shortcuts import render
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ProductForm
from .models import CartItem, Order, Product, ShippingAddress
from .serializers import UpdateCartSerializer, ShippingInformationSerializer

# Create your views here.

def store(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'store/store.html',context)

def cart(request):
    customer = request.user.customer
    order = Order.objects.get(customer=customer, complete=False)

    cart_items = order.cartitem_set.all()

    context = {'cart_items': cart_items, 'order_total': order.get_cart_total}
    return render(request, 'store/cart.html', context)


def checkout(request):
    customer = request.user.customer
    order = Order.objects.get(customer=customer, complete=False)

    cart_items = order.cartitem_set.all()

    context = {'cart_items': cart_items, 'order_total': order.get_cart_total}
    return render(request, 'store/checkout.html', context)


def add_product(request):
    product_form = ProductForm(request.POST or None, request.FILES or None)

    if product_form.is_valid():
        product_form.save()
        product_form = ProductForm()

    context = {
        'product_form': product_form
    }


    return render(request, 'store/add_product.html', context)

@api_view(['POST'])
def update_cart(request):
    serializer = UpdateCartSerializer(data=request.data)
    customer = request.user.customer

    if serializer.is_valid():
        data = serializer.validated_data
        product_id = data.get('productId')
        action = data.get('action')

        product = Product.objects.get(id=product_id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        cart_item, created = CartItem.objects.get_or_create(order=order, product=product)

        if action == 'add': 
            cart_item.quantity += 1
            print(cart_item.quantity)
        elif action == 'remove':
            cart_item.quantity -= 1
            print(cart_item.quantity)
        
        cart_item.save()

        if cart_item.quantity <= 0:
            cart_item.delete()
        
        return Response({'product':product.name , 'quantity: ': cart_item.quantity}, status=200)

    return Response({"message":'Invalid data'}, status=400)

@api_view(['GET'])
def cart_items(request):
    customer = request.user.customer
    order = Order.objects.get(customer=customer, complete=False)

    if order:
        cart_items = order.get_cart_items
    else:
        cart_items = 0
    return Response({'cart_items': cart_items})


@api_view(['POST'])
def process_order(request):
    serializer = ShippingInformationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        transaction_id = datetime.now().timestamp()
        customer = request.user.customer
        order = Order.objects.get(customer=customer, complete=False)

        ShippingAddress.objects.create (
            customer = customer,
            order = order,
            location = data.get('location'),
            estate = data.get('estate'),
            house_number = data.get('house_no')
        )

        order.transaction_id = transaction_id
        order.complete = True
        order.save()
        return Response({'Transaction ID': order.transaction_id, 'Order Status': order.complete})

    return Response({'message': 'Bad request'}, status=400)