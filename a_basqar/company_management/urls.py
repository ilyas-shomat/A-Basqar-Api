from django.urls import path
from . import views

urlpatterns = [

    ############ Stores #############
    path('stores/', views.get_all_users_company_stores, name="get_all_users_company_stores"),
    path('stores/create', views.create_new_store, name="create_new_store"),
    path('stores/update/<int:store_id>', views.update_store_info, name="update_store_info"),
    path('stores/delete/<int:store_id>', views.delete_one_account, name="delete_one_account"),

    ############ Company #############
    path('company/create', views.registration_new_company, name="registration_new_company"),
]
