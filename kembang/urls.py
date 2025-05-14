# pelayanan/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tentang/', views.tentang, name='tentang'),
    path('profil/', views.profil, name='profil'),
    path('ajukan/', views.ajukan_surat, name='ajukan'),
    path('status/', views.status_surat, name='status'),
    path('semua/', views.semua_pengajuan, name='semua_pengajuan'),
    path('login/', views.custom_login, name='login'),
]

