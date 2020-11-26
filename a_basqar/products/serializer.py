from rest_framework import serializers

from .models import (
    Common_Category,
    Each_Company_Category,
    Common_Product,
    Each_Company_Product,
    Each_Store_Product
)


class CommonCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Common_Category
        fields = "__all__"


class EachCompanyCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Each_Company_Category
        fields = "__all__"


class CommonProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common_Product
        fields = "__all__"


class EachCompanyProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Each_Company_Product
        fields = "__all__"


class EachStoreProductProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Each_Store_Product
        fields = "__all__"