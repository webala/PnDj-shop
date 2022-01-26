import imp
from django.urls import path
from .views import (
    store,
    cart,
    checkout,
    add_product,
    update_cart
)

urlpatterns = [
    path('', store, name='store'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('product/add', add_product, name='add_product'),
    path('update_cart', update_cart, name='update_cart'),
]