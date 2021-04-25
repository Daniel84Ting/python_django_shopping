from django.urls import path
from .views import *

# app_name = "shopping"

urlpatterns = [
    path('', views_index, name='shopping_index'),
    # path('show/<uuid:pk>', view_show, name='shopping_show')
]