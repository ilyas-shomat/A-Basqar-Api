from django.db import models
# from account.models import Account

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_bin = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.company_name


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=255)
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