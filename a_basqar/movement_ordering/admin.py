from django.contrib import admin

from .models import (
    MovementObject,
    MovementProduct,
    OrderingObject,
    OrderingProduct,
)
# Register your models here.
admin.site.register(MovementObject)
admin.site.register(MovementProduct)
admin.site.register(OrderingObject)
admin.site.register(OrderingProduct)


