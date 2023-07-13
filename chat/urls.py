from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:room>/', views.room, name="room"),
    path('checkview', views.checkview, name="checkview"),
    path('send/<str:room>/', views.send, name="send"),
    path('getMessage/<str:room>/', views.getMessage, name="getMessage"),
]
