from django.urls import path
from . import views

urlpatterns = [

    ############ Stores #############
    path('stores/', views.get_all_users_company_stores, name="get_all_users_company_stores"),
]
