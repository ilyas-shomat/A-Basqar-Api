from django.db import models


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
