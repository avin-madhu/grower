from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    # < > is used to pass dynamic values
    path('room/<str:roomkey>/', views.room, name="room"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:roomkey>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:roomkey>/', views.deleteRoom, name="delete-room"),
]