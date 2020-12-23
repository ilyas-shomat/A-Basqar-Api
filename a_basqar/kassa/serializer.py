from rest_framework import serializers

from .models import (
    IncomeKassaObject
)
from company_management.serializers import (
    ContragentSerializer
)
from export_import_products.serializer import (
    ExShoppingCartObjSerializer
)


class IncomeKassaObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeKassaObject
        fields = "__all__"


class GetIncomeKassaHistoryObjectsSerializer(serializers.ModelSerializer):
    # contragent = ContragentSerializer(read_only=True)
    export_object = ExShoppingCartObjSerializer(read_only=True)

    class Meta:
        model = IncomeKassaObject
        fields = "__all__"


# class CreateNewIncomeKassaObjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IncomeKassaObject
#         fields = ('export_object', 'fact_cash', 'comment', 'contragent')


class CreateNewIncomeKassaWithExport(serializers.ModelSerializer):
    class Meta:
        model = IncomeKassaObject
        fields = ('export_object', 'fact_cash', 'comment')

class CreateNewIncomeKassaWithContragent(serializers.ModelSerializer):
    class Meta:
        model = IncomeKassaObject
        fields = ('contragent', 'fact_cash', 'comment')