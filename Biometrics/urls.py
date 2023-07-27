from django.urls import path

from . import views

urlpatterns = [
    path('biometrics', views.showBiometrics, name='biometrics')
]