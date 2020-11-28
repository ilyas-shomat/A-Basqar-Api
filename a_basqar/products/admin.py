from django.contrib import admin

from .models import (
    CommonCategory,
    CompanyCategory,
    CommonProduct,
    CompanyProduct,
    StoreProduct
)

admin.site.register(CommonCategory)
admin.site.register(CompanyCategory)
admin.site.register(CommonProduct)
admin.site.register(CompanyProduct)
admin.site.register(StoreProduct)