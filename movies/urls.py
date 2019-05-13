from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    # path('new/', views.new_movie, name='new_movie'),
    path('<str:country_name>/', views.country_box_office),
    path('<str:country_id>/<int:rank>/', views.movie_detail),
]