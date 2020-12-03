from django.contrib import admin

from .models import (
    ImShoppingCartObject,
    ImportProducts
)

admin.site.register(ImShoppingCartObject)
admin.site.register(ImportProducts)

