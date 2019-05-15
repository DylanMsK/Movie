from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('<str:country>/', views.country_boxoffice, name='country_boxoffice'),
    path('<str:country>/<int:rank>/', views.country_detail, name='country_detail'),
]