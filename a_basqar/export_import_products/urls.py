from django.urls import path
from . import views

urlpatterns = [
    ############ IMPORT SHOPPING CART #############
    path('import_shopping_cart', views.get_current_import_shopping_cart,
         name="get_current_import_shopping_cart"),
]
