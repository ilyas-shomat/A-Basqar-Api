from rest_framework import serializers

from .models import (
    ReportingProduct
)
# class GetCashReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ("start_date", "end_date")

class ReportingProductSerializer(serializers.Serializer):
    prod_id = serializers.IntegerField()
    prod_name = serializers.CharField(max_length=200)
    count_on_start = serializers.CharField(max_length=200)
    count_on_end = serializers.CharField(max_length=200)
    import_count = serializers.CharField(max_length=200)
    export_count = serializers.CharField(max_length=200)

    # def __init__(self, prod_id, prod_name, count_on_start, count_on_end, income, expense):
    #     self.prod_id = prod_id
    #     self.prod_name = prod_name
    #     self.count_on_start = count_on_start
    #     self.count_on_end = count_on_end
    #     self.income = income
    #     self.expense = expense