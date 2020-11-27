from django.urls import path
from . import views

urlpatterns = [
    ############ Common #############
    path('common_categories', views.get_all_common_categories, name="get_all_common_categories"),

    ############ Category #############
    path('categories', views.get_each_company_categories, name="get_each_company_categories"),

    ############ Products #############
    path('products/<int:category_id>', views.get_each_company_products_in_selected_category, name="get_each_company_products_in_selected_category"),
]

