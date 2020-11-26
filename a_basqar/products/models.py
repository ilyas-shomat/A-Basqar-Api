from django.db import models
from company_management.models import (
    Company,
    Store,
)

# Create your models here.

class Common_Category(models.Model):
    common_category_id = models.AutoField(primary_key=True)
    common_category_name = models.CharField(max_length=255)
    common_category_level = models.IntegerField()

    def __str__(self):
        return self.common_category_name + " " + str(self.common_category_level)

class Each_Company_Category(models.Model):
    each_company_category_id = models.AutoField(primary_key=True)
    each_company_category_name = models.CharField(max_length=255)
    each_company_category_level = models.IntegerField()
    each_company_category_company = models.ForeignKey(Company,
                                                      on_delete=models.CASCADE,
                                                      related_name='each_company_category_company',
                                                      null=True)

    def __str__(self):
        return self.each_company_category_name + " " + str(self.each_company_category_level)


class Common_Product(models.Model):
    common_product_id = models.AutoField(primary_key=True)
    common_product_name = models.CharField(max_length=255)
    common_product_category = models.ForeignKey(Common_Category,
                                                on_delete=models.CASCADE,
                                                related_name='common_product_category',
                                                null=True)
    common_product_barcode = models.CharField(max_length=255)

    def __str__(self):
        return self.common_product_name

class Each_Company_Product(models.Model):
    each_company_product_id = models.AutoField(primary_key=True)
    each_company_product_name = models.CharField(max_length=255)
    each_company_product_category = models.ForeignKey(Each_Company_Category,
                                                on_delete=models.CASCADE,
                                                related_name='each_company_product_category',
                                                null=True)
    each_company_product_barcode = models.CharField(max_length=255)
    each_company_product_import_price = models.IntegerField(default=0)
    each_company_product_export_price = models.IntegerField(default=0)
    each_company_product_in_company = models.ForeignKey(Company,
                                                     on_delete=models.CASCADE,
                                                     related_name='each_company_product_company',
                                                     null=True)
    def __str__(self):
        return self.each_company_product_name

class Each_Store_Product(models.Model):
    each_store_product_id = models.AutoField(primary_key=True)
    each_store_product_in_company_product = models.ForeignKey(Each_Company_Product,
                                                     on_delete=models.CASCADE,
                                                     related_name='each_store_product_in_company_product',
                                                     null=True)
    each_store_product_amount = models.IntegerField()

    def __str__(self):
        return self.each_store_product_in_company_product.__str__()
