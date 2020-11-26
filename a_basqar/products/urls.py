from django.urls import path
from . import views

urlpatterns = [
    ############ Common #############
    path('common_companies/', views.get_all_common_categories, name="get_all_common_categories"),
]