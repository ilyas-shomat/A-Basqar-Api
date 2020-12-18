from django.db import models
from django.utils.crypto import get_random_string
from company_management.models import (
    Contragent
)
from export_import_products.models import (
    ImShoppingCartObject
)
from account.models import (
    Account
)


class IncomeKassaObject(models.Model):
    income_id = models.AutoField(primary_key=True)
    income_name = models.CharField(max_length=255, null=True)
    income_status = models.CharField(max_length=255)
    fact_cash = models.CharField(max_length=255, null=True)
    cash_sum = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255, null=True)

    contragent = models.ForeignKey(Contragent,
                                   on_delete=models.CASCADE,
                                   related_name='contragent',
                                   null=True
                                   )

    import_object = models.ForeignKey(ImShoppingCartObject,
                                      on_delete=models.CASCADE,
                                      related_name='contragent',
                                      null=True
                                      )
    date = models.DateField()
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='contragent',
                                null=True
                                )

    def save(self, *args, **kwargs):
        self.income_name = get_random_string(length=32)
        super(IncomeKassaObject, self).save(*args, **kwargs)
