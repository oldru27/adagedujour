from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('signup', views.creercompte, name='creation'),
    path('signin', views.selogger, name='connection'),
    path('logout', views.sedeco, name='deconnection')
]