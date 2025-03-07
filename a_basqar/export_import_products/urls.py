from django.urls import path
from . import views

urlpatterns = [
    ############ IMPORT SHOPPING CART #############
    path('import_cart', views.get_current_import_shopping_cart,
         name="get_current_import_shopping_cart"),
    path('get_current_import_object', views.get_current_import_object,
         name="get_current_import_object"),
    path('create_new_import_cart_object', views.create_new_import_cart_object,
         name="create_new_import_cart_object"),
    path('add_prods_to_im_shop', views.add_product_to_import_cart,
         name="addProductToImportCart"),
    path('edit_product_count_in_import_cart', views.edit_product_count_in_import_cart,
         name="edit_product_count_in_import_cart"),
    path('delete_product_count_in_import_cart', views.delete_product_count_in_import_cart,
         name="delete_product_count_in_import_cart"),
    path('get_import_history', views.get_import_history,
         name="get_import_history"),
    path('get_import_history_item/<int:import_id>', views.get_import_history_item,
         name="get_import_history_item"),
    path('buy_new_products', views.make_import_history,
         name="make_import_history"),


    ############ IMPORT SHOPPING CART #############
    path('export_cart', views.get_current_export_shopping_cart,
         name="get_current_export_shopping_cart"),
    path('get_current_export_object', views.get_current_export_object,
         name="get_current_export_object"),
    path('create_new_export_cart_object', views.create_new_export_cart_object,
         name="create_new_export_cart_object"),
    path('add_prods_to_ex_shop', views.add_product_to_export_cart,
         name="add_product_to_export_cart"),
    path('edit_product_count_in_export_cart', views.edit_product_count_in_export_cart,
         name="edit_product_count_in_export_cart"),
    path('delete_product_count_in_export_cart', views.delete_product_count_in_export_cart,
         name="delete_product_count_in_export_cart"),
    path('get_export_history', views.get_export_history,
         name="get_export_history"),
    path('get_export_history_item/<int:export_id>', views.get_export_history_item,
         name="get_export_history_item"),
    path('sell_new_products', views.make_export_history,
         name="make_export_history"),
    path('get_prods/<int:cat_id>', views.get_exact_category_products,
         name="get_exact_category_products"),
]
