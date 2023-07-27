from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.showHome, name="home"),
    path('', views.showLogin, name="invigilator-login"),
    path('logout', views.logout, name='logout'),
    path('update-user', views.updateUser, name='update-user'),
    path('settings/', views.showSettings, name='settings'),
    
 
]