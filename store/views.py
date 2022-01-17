from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class Store(ListView):
    paginate_by = 10
    model = Product
    context_object_name = 'products'
    template_name = 'store/store.html'


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_order_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context=context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_order_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context=context)
