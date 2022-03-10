from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerialzier


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    lookup_field = "pk"  # this one is default
