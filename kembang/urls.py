# pelayanan/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ajukan/', views.ajukan_surat, name='ajukan_surat'),
    path('riwayat/', views.riwayat_surat, name='riwayat_surat'),
    path('semua/', views.semua_pengajuan, name='semua_pengajuan'),
]
