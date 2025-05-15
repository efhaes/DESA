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
    path('akta-kematian/', views.ajukan_akta_kematian, name='ajukan_akta_kematian'),
    path('akta-kelahiran/', views.ajukan_akta_kelahiran, name='ajukan_akta_kelahiran'),
    path('pindah-datang/', views.ajukan_pindah_datang, name='ajukan_pindah_datang'),
    path('pindah-keluar/', views.ajukan_pindah_keluar, name='ajukan_pindah_keluar'),
    path('update/<int:surat_id>/', views.update_status, name='update_status'),
    path('login/', views.login_view, name='login'),

]

