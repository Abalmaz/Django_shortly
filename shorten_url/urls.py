from django.urls import path
from shorten_url import views

urlpatterns = [
    path('', views.UrlView.as_view()),
    path('/<pk>/$', views.detail),
    path('visit_url/<short_url>', views.redirect_to_url),
]