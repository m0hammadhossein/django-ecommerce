import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class Store(ListView):
    paginate_by = 10
    model = Product
    context_object_name = 'products'
    template_name = 'store/store.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cartItems = order.get_order_items
        else:
            order = {'get_cart_total': 0, 'get_order_items': 0}
            cartItems = order['get_order_items']
        context.update({'order': order, 'cartItems': cartItems})
        return context



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_order_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_order_items': 0}
        cartItems = order['get_order_items']

    context = {'items': items, 'order': order, 'cartItems':cartItems}
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


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
