# pelayanan/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ajukan_surat, name='pelayanan'),
]
