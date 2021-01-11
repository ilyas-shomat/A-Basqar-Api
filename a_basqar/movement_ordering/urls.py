from django.urls import path
from . import views

urlpatterns = [
    ############ MOVEMENT #############
    path('movement_cart', views.get_movement_cart,
         name="get_movement_cart"),
]
