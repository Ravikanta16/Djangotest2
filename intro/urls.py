from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    #path('room/', views.room, name='room'),
    path('room/<str:pk>/', views.room, name='room'),
]