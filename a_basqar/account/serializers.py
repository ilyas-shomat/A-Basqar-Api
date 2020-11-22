from rest_framework import serializers
from . import models
from company_management.serializers import CompanySerializer, StoreSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = "__all__"
        extra_kwargs = {
            # 'password': {'write_only':True},
            'is_admin': {'write_only': True},
            'is_active': {'write_only': True},
            'is_staff': {'write_only': True},
            'is_superuser': {'write_only': True},
        }

    def save(self):
        account = models.Account(full_name=self.validated_data['full_name'],
                                 username=self.validated_data["username"],
                                 status=self.validated_data["status"],
                                 store=self.validated_data["store"],
                                 company=self.validated_data["company"])
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account


class AccountPropertiesSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    # company = CompanySerializer(read_only=True)

    class Meta:
        model = models.Account
        fields = "__all__"
        extra_kwargs = {
            # 'password': {'write_only':True},
            'is_admin': {'write_only': True},
            'is_active': {'write_only': True},
            'is_staff': {'write_only': True},
            'is_superuser': {'write_only': True},
        }


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    # confirm_new_password = serializers.CharField(required=True)
