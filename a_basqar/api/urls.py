from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, StoreViewSet

# router = DefaultRouter()
# router.register(r'companies', CompanyViewSet)
# router.register(r'stores', StoreViewSet)
# urlpatterns = router.urls
"""a_basqar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

]
