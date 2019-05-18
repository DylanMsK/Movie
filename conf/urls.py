"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from movies import views as movies_views


urlpatterns = [
    path('', movies_views.index, name='index'),
    path('godmin/', admin.site.urls),
    path('netflix/', movies_views.netflix_list, name='netflix_list'),
    path('netflix/<int:rank>/', movies_views.netflix_detail, name='netflix_detail'),
    path('movies/', include('movies.urls')),
]

handler404 = 'movies.views.page_not_found'
handler500 = 'movies.views.server_error'