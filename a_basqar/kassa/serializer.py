from rest_framework import serializers

from .models import (
    IncomeKassaObject
)

class IncomeKassaObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeKassaObject
        fields = "__all__"
