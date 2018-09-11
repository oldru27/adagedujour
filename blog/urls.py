from django.urls import path
from . import views


urlpatterns = [
    path('', views.listblog, name='listblog'),
    path('<int:blog_id>/', views.detail, name='detailblog'), #ca veut duire cherche un int derriere blog et on le save en blog_id
]