from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_resorts, name='home'),
    path('resorts-page/', views.resorts_page, name='resorts-page'),
    path('favorite-resorts/', views.favorite_resorts, name='favorite-resorts'),
    path('reservations/', views.reservations, name='reservations'),
    path('accounts/signup/', views.signup, name='signup'),
    path('add-favorite/<int:resort_id>/', views.add_favorite, name='add-favorite'),
    path('remove-favorite/<int:resort_id>/', views.remove_favorite, name='remove-favorite'),
    path('resort/<int:resort_id>/', views.resort_detail, name='resort-detail'),  
    path('resort/<int:resort_id>/reserve/', views.reserve_resort, name='reserve-resort'),
    path('reservation/<int:reservation_id>/cancel/', views.cancel_reservation, name='cancel-reservation'),
    path('reservation/<int:reservation_id>/update/', views.update_reservation, name='update-reservation'),
]
  