from django.urls import path
from . import views

urlpatterns = [
    ############ MOVEMENT #############
    path('movement_cart', views.get_movement_cart,
         name="get_movement_cart"),
    path('movement_object', views.get_current_movement_object,
         name="get_current_movement_object"),
    path('create_movement_object', views.create_new_movement_cart,
         name="create_movement_object"),
    path('add_prod_to_movement_cart', views.add_product_to_movement_cart,
         name="add_product_to_movement_cart"),
    path('edit_prod_count_in_movement_cart', views.edit_product_count_in_movement_cart,
         name="edit_product_count_in_movement_cart"),
    path('delete_prod_in_movement_cart', views.delete_product_count_in_movement_cart,
         name="delete_prod_in_cart"),
    path('make_movement_history', views.make_movement_history,
         name="make_movement_history"),
    path('get_movement_history', views.get_movement_history,
         name="get_movement_history"),
    path('get_movement_history/<int:movement_id>', views.get_movement_history_item,
         name="get_movement_history"),

   ############ MOVEMENT #############
   path('ordering_object', views.get_current_ordering_object,
         name="get_current_ordering_object"),
   path('ordering_cart', views.get_ordering_cart,
         name="get_ordering_cart"),
   path('create_ordering_object', views.create_new_ordering_cart,
         name="create_new_ordering_cart"),
   path('add_prod_to_ordering_cart', views.add_product_to_ordering_cart,
         name="add_product_to_ordering_cart"),
   path('edit_prod_count_in_ordering_cart', views.edit_product_count_in_ordering_cart,
         name="edit_product_count_in_ordering_cart"),
   path('delete_prod_in_ordering_cart', views.delete_product_count_in_ordering_cart,
         name="delete_product_count_in_ordering_cart"),
   path('make_ordering_open', views.make_ordering_object_open,
         name="make_ordering_object_open"),
   path('make_ordering_history', views.make_ordering_history,
         name="make_ordering_history"),
   path('get_all_open_ordering', views.get_open_ordering_list,
         name="get_open_ordering_list"),
   path('get_ordering_hsitory', views.get_ordering_history,
         name="get_ordering_history"),
   path('get_ordering_item/<int:ordering_id>', views.get_ordering_item,
         name="get_open_ordering_item"),

]
