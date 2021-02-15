from django.urls import path
from . import views

urlpatterns = [

    ############ Stores #############
    path('stores/', views.get_all_users_company_stores, name="get_all_users_company_stores"),
    path('stores/users_list/<int:store_id>', views.get_user_of_one_store, name="get_all_users_company_stores"),
    path('stores/create', views.create_new_store, name="create_new_store"),
    path('stores/update/<int:store_id>', views.update_store_info, name="update_store_info"),
    path('stores/delete/<int:store_id>', views.delete_one_account, name="delete_one_account"),

    ############ Company #############
    path('company/create', views.registration_new_company, name="registration_new_company"),
    path('company/users', views.get_companies_all_user, name="get_companies_all_user"),
    path('company/users/<int:account_id>', views.get_user_from_companies_users_list, name="get_user_from_companies_users_list"),
    path('company/users/accesses/<int:account_id>', views.get_users_access_funcs, name="get_users_access_funcs"),
    path('company/users/accesses/edit/<int:account_id>', views.edit_users_access_funcs, name="edit_users_access_funcs"),

    ############ Contragent #############
    path('contragent', views.get_users_contrs, name="get_users_contrs"),
    path('contragent/edit', views.edit_user_contr, name="edit_user_contr"),
    path('contragent/add', views.add_user_contr, name="add_user_contr"),


]
