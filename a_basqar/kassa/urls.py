from django.urls import path
from . import views

urlpatterns = [
    ############  INCOME KASSA #############
    path('income_kassa_objects', views.get_income_kassa_objects,
         name="get_income_kassa_objects"),
    path('income_kassa_history', views.get_income_kassa_history_objects,
         name="get_income_kassa_history_objects"),
    # path('create_new_income', views.create_new_income_kassa,
    #      name="create_new_income_kassa"),
    path('create_new_income_contr', views.create_new_income_kassa_contr,
         name="create_new_income_kassa_contr"),

]
