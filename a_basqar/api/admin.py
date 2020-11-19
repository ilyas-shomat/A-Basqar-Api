from django.contrib import admin
from .models import Company, Store, Account

# Register your models here.

admin.site.register(Company)
admin.site.register(Store)
admin.site.register(Account)