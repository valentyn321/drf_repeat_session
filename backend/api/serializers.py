from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        read_only=True,
    )
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # the code below was written only to practice with remind nested
    # serializers and this code doesn't have any practival sense

    # other_products = serializers.SerializerMethodField(read_only=True)

    # def get_other_products(self, obj):
    #     qs = obj.product_set.all()
    #     return UserProductInlineSerializer(
    #         qs,
    #         many=True,
    #         context=self.context,
    #     ).data
