from django.urls import path
from . import views

urlpatterns = [
    ############  INCOME KASSA #############
    path('income_kassa_objects', views.get_income_kassa_objects,
         name="get_income_kassa_objects"),
    path('income_kassa_history', views.get_income_kassa_history_objects,
         name="get_income_kassa_history_objects"),
]
