from django.urls import path
from . import views

urlpatterns = [
    path('<str:country_name>/', views.country_box_office),
    path('<str:country_id>/<int:rank>/', views.movie_detail),
]