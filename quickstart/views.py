from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status, response
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from quickstart.models import Order
from quickstart.serializers import OrderSerializer


class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        print('----------------------------------------------data', request.data['items'])
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer





