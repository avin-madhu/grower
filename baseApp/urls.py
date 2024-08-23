from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    # < > is used to pass dynamic values
    path('room/<str:roomkey>/', views.room, name="room"),

]