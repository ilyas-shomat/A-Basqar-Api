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
]
