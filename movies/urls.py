from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('netflix/', views.netflix_list, name='netflix_list'),
    path('netflix/<int:rank>/', views.netflix_detail, name='netflix_detail'),
    path('<str:country>/', views.country_boxoffice, name='country_boxoffice'),
    path('<str:country>/<int:rank>/', views.country_detail, name='country_detail'),
]