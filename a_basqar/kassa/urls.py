from django.urls import path
from . import views

urlpatterns = [
    ############  INCOME KASSA #############
    path('income_kassa_objects', views.get_income_kassa_objects,
         name="get_income_kassa_objects"),
    path('income_kassa_history', views.get_income_kassa_history_objects,
         name="get_income_kassa_history_objects"),
    path('create_new_income_export', views.create_new_income_kassa_export,
         name="create_new_income_kassa_export"),
    path('create_new_income_contr', views.create_new_income_kassa_contr,
         name="create_new_income_kassa_contr"),

    ############  EXPENSE KASSA #############
    path('expense_kassa_history', views.get_expense_kassa_history_objects,
         name="get_expense_kassa_history_objects"),
    path('create_new_expense_export', views.create_new_expense_kassa_import,
         name="create_new_expense_kassa_import"),
    path('create_new_expense_contr', views.create_new_expense_kassa_contr,
         name="create_new_expense_kassa_contr"),

]
