from django.contrib import admin

from .models import (
    Common_Category,
    Each_Company_Category,
    Common_Product,
    Each_Company_Product,
    Each_Store_Product
)

admin.site.register(Common_Category)
admin.site.register(Each_Company_Category)
admin.site.register(Common_Product)
admin.site.register(Each_Company_Product)
admin.site.register(Each_Store_Product)