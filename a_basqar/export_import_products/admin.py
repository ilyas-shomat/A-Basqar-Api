from django.contrib import admin

from .models import (
    ImShoppingCartObject,
    ImportProduct,
    ExShoppingCartObject,
    ExportProduct
)

admin.site.register(ImShoppingCartObject)
admin.site.register(ImportProduct)
admin.site.register(ExShoppingCartObject)
admin.site.register(ExportProduct)


