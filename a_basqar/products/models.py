import uuid

from django.db import models
from company_management.models import (
    Company,
    Store,
)


# Create your models here.


class CommonCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_level = models.IntegerField()

    category_index_id = models.UUIDField(default=uuid.uuid4,
                                         editable=False,
                                         unique=True,
                                         null=True)

    def __str__(self):
        return self.category_name + " " + str(self.category_level)


class CompanyCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_level = models.IntegerField()
    category_company = models.ForeignKey(Company,
                                         on_delete=models.CASCADE,
                                         related_name='category_company',
                                         null=True)

    category_index_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.category_name + " " + str(self.category_level)


class CommonProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_category = models.ForeignKey(CommonCategory,
                                         on_delete=models.CASCADE,
                                         related_name='product_category',
                                         null=True)
    product_barcode = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name


class CompanyProduct(models.Model):
    DoesNotExixt = None
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_category = models.ForeignKey(CompanyCategory,
                                         on_delete=models.CASCADE,
                                         related_name='product_category',
                                         null=True)
    product_barcode = models.CharField(max_length=255)
    product_import_price = models.IntegerField(default=0)
    product_export_price = models.IntegerField(default=0)
    product_company = models.ForeignKey(Company,
                                        on_delete=models.CASCADE,
                                        related_name='each_company_product_company',
                                        null=True)

    def __str__(self):
        return self.product_name


class StoreProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    company_product = models.ForeignKey(CompanyProduct,
                                        on_delete=models.CASCADE,
                                        related_name='company_product',
                                        null=True)
    product_amount = models.IntegerField()

    def __str__(self):
        return self.company_product.__str__()
