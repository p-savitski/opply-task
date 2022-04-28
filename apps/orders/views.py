from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import Order
from apps.orders.serializers import OrderCreateSerializer, OrderListSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderCreateSerializer


class OrderListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('ordered_items')
