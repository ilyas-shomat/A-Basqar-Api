from django.urls import path
from . import views

urlpatterns = [
    ############ IMPORT SHOPPING CART #############
    path('import_shopping_cart', views.get_current_import_shopping_cart,
         name="get_current_import_shopping_cart"),
    path('get_current_import_object', views.get_current_import_object,
         name="get_current_import_object"),
    path('create_new_import_cart_object', views.create_new_import_cart_object,
         name="create_new_import_cart_object"),
    path('add_prods_to_im_shop', views.add_product_to_import_cart,
         name="addProductToImportCart"),
    path('edit_product_count_in_import_cart', views.edit_product_count_in_import_cart,
         name="edit_product_count_in_import_cart")
]
