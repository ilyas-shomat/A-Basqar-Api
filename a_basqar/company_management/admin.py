from django.contrib import admin

# Register your models here.
from .models import Company, Store, AccessFunc

admin.site.register(Company)
admin.site.register(Store)
admin.site.register(AccessFunc)