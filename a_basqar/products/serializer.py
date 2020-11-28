from rest_framework import serializers

from .models import (
    CommonCategory,
    CompanyCategory,
    CommonProduct,
    CompanyProduct,
    StoreProduct
)


class CommonCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CommonCategory
        fields = "__all__"


class EachCompanyCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyCategory
        fields = "__all__"


class CommonProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonProduct
        fields = "__all__"


class EachCompanyProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyProduct
        fields = "__all__"


class EachStoreProductProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreProduct
        fields = "__all__"