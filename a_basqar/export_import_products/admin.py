from django.contrib import admin

from .models import (
    ImShoppingCartObject,
    ImportProduct
)

admin.site.register(ImShoppingCartObject)
admin.site.register(ImportProduct)

