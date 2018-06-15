from django.urls import path
from shorten_url import views

urlpatterns = [
    path('', views.index),
    path('shortly', views.shorten),
    path('visit_url/<short_url>', views.redirect_to_url),
]