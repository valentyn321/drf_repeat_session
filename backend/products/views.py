from tracemalloc import get_object_traceback
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerialzier


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    GET method - returns a list of Products
    POST method  - creates a new Product instance
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerialzier

    def perform_create(self, serializer):
        # also, very common usage is sending Django signals to db
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content", None)
        if content is None:
            content = title
        serializer.save(content=content)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier


class ProductDetailAPIView(generics.RetrieveAPIView):
    # is not currently using, because here is a ListCreateView
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    # lookup_field = 'pk'


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.content is None:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    lookup_field = "pk"

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    """
    This function shows how those generics are written
    Nice for understanding how it worksm but bad one for
    using in the production
    """
    if request.method == "GET":
        if pk is not None:
            instance = get_object_or_404(Product, pk=pk)  # can throw Http404
            data = ProductSerialzier(instance, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerialzier(queryset, many=True).data
        return Response(data)
    elif request.method == "POST":
        serializer = ProductSerialzier(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content", None)
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "invalid request"}, status=400)
