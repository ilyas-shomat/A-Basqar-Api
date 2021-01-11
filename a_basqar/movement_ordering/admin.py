from django.contrib import admin

from .models import (
    MovementObject,
    MovementProduct
)
# Register your models here.
admin.site.register(MovementObject)
admin.site.register(MovementProduct)

