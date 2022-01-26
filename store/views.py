from django.shortcuts import render
from .forms import ProductForm
from .models import Product
# Create your views here.

def store(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'store/store.html',context)

def cart(request):
    return render(request, 'store/cart.html')


def checkout(request):
    return render(request, 'store/checkout.html')


def add_product(request):
    product_form = ProductForm(request.POST or None, request.FILES or None)

    if product_form.is_valid():
        product_form.save()
        product_form = ProductForm()

    context = {
        'product_form': product_form
    }


    return render(request, 'store/add_product.html', context)

def update_cart(request):
    return 