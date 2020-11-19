from rest_framework import serializers
from . import models


class CompanySerializer(serializers.ModelSerializer):
    # stores = StoreSerializer()

    class Meta:
        model = models.Company
        # fields = ('company_id', 'company_name', 'company_bin')
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(read_only=True)

    class Meta:
        model = models.Store
        fields = "__all__"

# Working code
class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only':True}
        }

# class AccountSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Account
#         fields = "__all__"
#         extra_kwargs = {
#                 'password': {'write_only':True}
#         }
#
#     def save(self):
#         account = models.Account(full_name=self.validated_data['full_name'],
#                                  login=self.validated_data["login"],
#                                  password=self.validated_data["password"],
#                                  status=self.validated_data["status"],
#                                  store=self.validated_data["store"],
#                                  company=self.validated_data["company"])
#         account.save()
#         return account