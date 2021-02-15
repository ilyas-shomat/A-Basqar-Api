from django.db import models
# from account.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_bin = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.company_name


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=255, default="Default")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='store_company', null=True)

    def __str__(self):
        return self.store_name

class AccessFunc(models.Model):
    user = models.ForeignKey("account.Account", on_delete=models.CASCADE, related_name='access_funs', null=True)
    access_id = models.AutoField(primary_key=True)
    import_products = models.BooleanField(default=True)
    export_products = models.BooleanField(default=True)
    import_kassa = models.BooleanField(default=True)
    export_kassa = models.BooleanField(default=True)
    movement = models.BooleanField(default=True)
    application = models.BooleanField(default=True)
    management = models.BooleanField(default=True)
    reports = models.BooleanField(default=True)
    profile = models.BooleanField(default=True)


class Contragent(models.Model):
    contragent_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    bin = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_contragent", null=True)

    def __str__(self):
        return self.name +", id:" + str(self.contragent_id)


@receiver(post_save, sender=Company)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Store.objects.create(company=instance)

