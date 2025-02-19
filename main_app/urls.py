from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_resorts, name='home'),
    path('resorts-page/', views.resorts_page, name='resorts-page'),
    path('favorite-resorts/', views.favorite_resorts, name='favorite-resorts'),
    path('reservations/', views.reservations, name='reservations'),
    path('accounts/signup/', views.signup, name='signup'),
]
  