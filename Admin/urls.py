from django.urls import path
from . import views



urlpatterns = [
    path('home', views.showAdminIndex, name="show-index"),
]







