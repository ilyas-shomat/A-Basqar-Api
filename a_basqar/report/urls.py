from django.urls import path
from . import views

urlpatterns = [
    ############  CASH REPORT #############
    path('cash_report', views.get_cash_report,
    name="get_cash_report"),
    
    ############  CASH REPORT #############
    path('prod_report', views.get_product_report,
    name="get_prod_report"),
]