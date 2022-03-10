from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title


class ProductSerialzier(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
    )
    title = serializers.CharField(validators=[validate_title])
    owner = UserPublicSerializer(source="user", read_only=True)

    class Meta:
        model = Product
        fields = [
            "owner",
            "url",
            "edit_url",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    def get_edit_url(self, obj):
        if self.context.get("request") is None:
            return None
        return reverse(
            "product-update",
            kwargs={"pk": obj.pk},
            request=self.context.get("request"),
        )

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        return obj.get_discount()
