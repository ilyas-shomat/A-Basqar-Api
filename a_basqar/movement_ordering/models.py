from django.db import models

from products.models import (
    StoreProduct
)
from account.models import (
    Account,
    Store
)
# Create your models here.
class MovementObject(models.Model):
    movement_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='movement_account',
                                null=True)

    status = models.CharField(max_length=255)
    store = models.ForeignKey(Store,
                            on_delete=models.CASCADE,
                            related_name='movement_store',
                            null=True)

    date = models.DateField(null=True)

    def __str__(self):
        return "movement object with id: " + str(self.movement_id) + ", status: " + self.status


class MovementProduct(models.Model):
    movement_prod_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='movement_prod_account',
                                null=True) 

    movement_product = models.ForeignKey(StoreProduct,
                                         on_delete=models.CASCADE,
                                         related_name='movement_product',
                                         null=True)
    movement_object = models.ForeignKey(MovementObject,
                                        on_delete=models.CASCADE,
                                        related_name='movement_object',
                                        null=True)
    product_amount = models.IntegerField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.movement_object.__str__() + " count: " + str(self.product_amount) + " date: " + str(self.date)
