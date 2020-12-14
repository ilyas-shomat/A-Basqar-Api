from django.urls import path
from . import views

urlpatterns = [
    ############ IMPORT SHOPPING CART #############
    path('import_shopping_cart', views.get_current_import_shopping_cart,
         name="get_current_import_shopping_cart"),
    path('get_current_import_object', views.get_current_import_object,
         name="get_current_import_object"),
    path('add_prods_to_im_shop', views.add_product_to_import_cart,
         name="addProductToImportCart"),
]
