from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.products.models import Product
from apps.products.serizlizers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
