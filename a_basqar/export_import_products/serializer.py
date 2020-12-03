from rest_framework import serializers

from .models import (
    ImShoppingCartObject,
    ImportProducts
)


class ImShoppingCartObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImShoppingCartObject
        fields = "__all__"


class ImportProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportProducts
        fields = "__all__"
