from django.urls import path

from quickstart.views import OrderList, OrderCreate

urlpatterns = [
    path('orders/', OrderList.as_view(), name='order_list'),
    path('orders/create', OrderCreate.as_view(), name='order_create'),
    path('orders/<int:id>/', OrderCreate.as_view(), name='order_detail'),
]
