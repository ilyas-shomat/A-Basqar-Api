from django.db import models

from products.models import (
    StoreProduct
)
from account.models import (
    Account
)
from company_management.models import (
    Contragent
)


class ImShoppingCartObject(models.Model):
    im_shopping_cart_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='account',
                                null=True)

    status = models.CharField(max_length=255)
    import_contragent = models.ForeignKey(Contragent,
                                   on_delete=models.CASCADE,
                                   related_name='import_contragent',
                                   null=True)
    date = models.DateField(null=True)
    cash_sum = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "import cart object with id: " + str(self.im_shopping_cart_id) + ", status: " + self.status


class ImportProduct(models.Model):
    im_prod_id = models.AutoField(primary_key=True)
    import_product = models.ForeignKey(StoreProduct,
                                       on_delete=models.CASCADE,
                                       related_name='import_product',
                                       null=True)

    im_shopping_car_obj = models.ForeignKey(ImShoppingCartObject,
                                            on_delete=models.CASCADE,
                                            related_name='im_shopping_car_obj',
                                            null=True)
    prod_amount_in_cart = models.IntegerField(null=True)

    def __str__(self):
        return self.import_product.__str__() + " count: " +str(self.prod_amount_in_cart)


class ExShoppingCartObject(models.Model):
    ex_shopping_cart_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='export_contragent',
                                null=True)

    status = models.CharField(max_length=255)

    export_contragent = models.ForeignKey(Contragent,
                                   on_delete=models.CASCADE,
                                   related_name='export_product',
                                   null=True)
    date = models.DateField(null=True)
    cash_sum = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "export cart object with id: " + str(self.ex_shopping_cart_id) + ", status: " + self.status


class ExportProduct(models.Model):
    ex_prod_id = models.AutoField(primary_key=True)
    export_product = models.ForeignKey(StoreProduct,
                                       on_delete=models.CASCADE,
                                       related_name='export_product',
                                       null=True)

    ex_shopping_car_obj = models.ForeignKey(ExShoppingCartObject,
                                            on_delete=models.CASCADE,
                                            related_name='ex_shopping_car_obj',
                                            null=True)
    prod_amount_in_cart = models.IntegerField(null=True)

    def __str__(self):
        return self.export_product.__str__() + " count: " +str(self.prod_amount_in_cart)
