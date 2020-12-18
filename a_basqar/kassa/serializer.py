from rest_framework import serializers

from .models import (
    IncomeKassaObject
)
from company_management.serializers import (
    ContragentSerializer
)
from export_import_products.serializer import (
    ImShoppingCartObjSerializer
)




class IncomeKassaObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeKassaObject
        fields = "__all__"


class GetIncomeKassaHistoryObjectsSerializer(serializers.ModelSerializer):
    contragent = ContragentSerializer(read_only=True)
    import_object = ImShoppingCartObjSerializer(read_only=True)
    class Meta:
        model = IncomeKassaObject
        fields = "__all__"

class CreateNewIncomeKassaObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeKassaObject
        fields = ('')