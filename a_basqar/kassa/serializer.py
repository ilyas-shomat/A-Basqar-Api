from rest_framework import serializers

from .models import (
    IncomeKassaObject,
    ExpenseKassaObject
)
from company_management.serializers import (
    ContragentSerializer
)
from export_import_products.serializer import (
    ExShoppingCartObjSerializer,
    ImShoppingCartObjSerializer
)


# ///////////////////////// INCOME KASSA //////////////////////

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


class CreateNewIncomeKassaWithExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeKassaObject
        fields = ('export_object', 'fact_cash', 'comment')


class CreateNewIncomeKassaWithContragentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeKassaObject
        fields = ('contragent', 'fact_cash', 'comment')


# ///////////////////////// EXPENSE KASSA //////////////////////

class ExpenseKassaObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseKassaObject
        fields = "__all__"


class GetExpenseKassaHistoryObjectsSerializer(serializers.ModelSerializer):
    import_object = ImShoppingCartObjSerializer(read_only=True)

    class Meta:
        model = ExpenseKassaObject
        fields = "__all__"


class CreateNewExpenseKassaWithImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseKassaObject
        fields = ('import_object', 'fact_cash', 'comment')


class CreateNewExpenseKassaWithContragentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseKassaObject
        fields = ('contragent', 'fact_cash', 'comment')
