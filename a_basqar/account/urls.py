from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [

    ############ Common #############
    path('accounts/', views.get_all_accounts, name="get_all_accounts"),

    ############ Auth #############
    path('login', obtain_auth_token, name="login"),
    path('accounts/create/', views.post_one_account, name="account_create"),

    ############ Profile #############
    path('profile', views.get_profile_info, name="profile"),
    path('profile/update', views.put_one_account, name="profile_update"),
    path('change_password', views.ChangePasswordView.as_view(), name="change_password"),
]
