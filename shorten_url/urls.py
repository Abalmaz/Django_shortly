from django.urls import path
from shorten_url import views

urlpatterns = [
    path('', views.index),
    path('shortly', views.shorten),
]