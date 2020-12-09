from django.db import models

from products.models import (
    StoreProduct
)

from account.models import (
    Account
)


class ImShoppingCartObject(models.Model):
    im_shopping_cart_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='account',
                                null=True)

    status = models.CharField(max_length=255)


class ImportProducts(models.Model):
    im_prod_id = models.AutoField(primary_key=True)
    import_product = models.ForeignKey(StoreProduct,
                                       on_delete=models.CASCADE,
                                       related_name='import_product',
                                       null=True)

    im_shopping_car_obj = models.ForeignKey(ImShoppingCartObject,
                                            on_delete=models.CASCADE,
                                            related_name='im_shopping_car_obj',
                                            null=True)

    def __str__(self):
        return self.import_product.__str__()
