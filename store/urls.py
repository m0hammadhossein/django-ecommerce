from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store.as_view(), name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

]
