from django.urls import path
from . import views

urlpatterns = [
    ############ MOVEMENT #############
    path('movement_cart', views.get_movement_cart,
         name="get_movement_cart"),
    path('movement_object', views.get_current_movement_object,
         name="get_current_movement_object"),
]
