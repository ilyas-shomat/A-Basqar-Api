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
    path('add_prod_to_cart', views.add_product_to_movement_cart,
         name="add_product_to_movement_cart"),
    path('edit_prod_count_in_cart', views.edit_product_count_in_movement_cart,
         name="edit_product_count_in_movement_cart"),
    path('delete_prod_in_cart', views.delete_product_count_in_movement_cart,
         name="delete_prod_in_cart"),
    path('make_movement_history', views.make_movement_history,
         name="make_movement_history"),
    path('get_movement_history', views.get_movement_history,
         name="get_movement_history"),
]
