from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('store/<int:company_id>', views.get_stores),
    path('companies/', views.get_post_companies),
    path('accounts/', views.get_all_accounts),

    path('accounts/<int:account_id>', views.get_one_account, name="account_detail"),
    path('accounts/delete/<int:account_id>', views.delete_one_account, name="account_delete"),
    path('accounts/update/<int:account_id>', views.put_one_account, name="account_update"),
    path('accounts/create/', views.post_one_account, name="account_create"),

    path('login', obtain_auth_token, name="login")

]
