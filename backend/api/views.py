from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerialzier


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerialzier(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid": "title was not injecsted"}, status=400)
