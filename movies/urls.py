from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<str:country_name>/', views.country_box_office),
    path('<str:country_name>/<int:rank>/', views_movie_detail),
]