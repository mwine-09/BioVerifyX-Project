from django.urls import path
from . import views



urlpatterns = [
    path('', views.showInvigilatorIndex, name="show-invigilator-index"),
    path('login', views.showLogin, name="login"),
    path('logout', views.logout, name='logout'),
    path('update-user', views.updateUser, name='update-user'),
    path('settings/', views.showSettings, name='settings'),
    
 
]