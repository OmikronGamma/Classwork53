"""
URL configuration for Classwork53 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from catalogue import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('movies/', views.Movieslist.as_view(), name='allmovies'),
    path('actors/', views.Actorslist.as_view(), name='allactors'),
    path('director/', views.Directorslist.as_view(), name='alldirectors'),
    # path('info/<int:id>/', views.movieinfo, name='movieinfo'),
    path('movie_info/<slug:pk>/<str:title>', views.Moviedetails.as_view(), name='movieinfo'),
    path('actor_info/<slug:pk>/<str:last_name>', views.Actordetails.as_view(), name='actorinfo'),
    path('director_info/<slug:pk>/<str:last_name>', views.Directordetails.as_view(), name='directorinfo'),
    path('user/', include('django.contrib.auth.urls')),
    path('subscr/', views.subscr, name='subscr'),
    path('subscr/watcher/<int:id1>/<int:id2>/<int:id3>', views.watcher, name='watcher'),
    path('subscr/buy/<int:type>', views.buy, name='buysub'),
    path('user/registration/', views.registration, name='registration'),
    path('submanager/', views.submanager, name='submanager'),
    path('switch_to_bronze/', views.switch_to_bronze, name='switch_to_bronze'),
    path('switch_to_silver/', views.switch_to_silver, name='switch_to_silver'),
    path('switch_to_gold/', views.switch_to_gold, name='switch_to_gold'),
]





'''
reset_form
reset_done
reset_confirm
reset_complete
'''