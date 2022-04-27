from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('../static/html/', views.productos),
]
