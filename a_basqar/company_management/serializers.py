from rest_framework import serializers

from .models import Company, Store

class CompanySerializer(serializers.ModelSerializer):
    # stores = StoreSerializer()

    class Meta:
        model = Company
        # fields = ('company_id', 'company_name', 'company_bin')
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Store
        fields = "__all__"