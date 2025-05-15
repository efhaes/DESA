# pelayanan/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('tentang/', views.tentang, name='tentang'),
    path('profil/', views.profil, name='profil'),
    path('ajukan/', views.ajukan_surat, name='ajukan'),
    path('status/', views.status_surat, name='status'),
    path('semua/', views.semua_pengajuan, name='semua_pengajuan'),
    
    path('surat/akta-kematian/', views.pengajuan_akta_kematian, name='pengajuan_akta_kematian'),
    path('admin/akta-kematian/', views.daftar_pengajuan_akta_kematian, name='daftar_pengajuan_akta_kematian'),
    path('admin/akta-kematian/<int:pk>/', views.detail_pengajuan_akta_kematian, name='detail_pengajuan_akta_kematian'),
    # Akta Kelahiran
    path('pengajuan/akta-kelahiran/', views.pengajuan_akta_kelahiran, name='pengajuan_akta_kelahiran'),
    path('admin/akta-kelahiran/', views.daftar_pengajuan_kelahiran, name='daftar_pengajuan_kelahiran'),
    path('admin/akta-kelahiran/<int:pk>/', views.detail_pengajuan_kelahiran, name='detail_pengajuan_kelahiran'),

    # Pindah Datang
    path('pengajuan/pindah-datang/', views.pengajuan_pindah_datang, name='pengajuan_pindah_datang'),
    path('admin/pindah-datang/', views.daftar_pindah_datang, name='daftar_pengajuan_pindah_datang'),
    path('admin/pindah-datang/<int:pk>/', views.detail_pindah_datang, name='detail_pengajuan_pindah_datang'),

    # Pindah Keluar
    path('pengajuan/pindah-keluar/', views.pengajuan_pindah_keluar, name='pengajuan_pindah_keluar'),
    path('admin/pindah-keluar/', views.daftar_pindah_keluar, name='daftar_pengajuan_pindah_keluar'),
    path('admin/pindah-keluar/<int:pk>/', views.detail_pindah_keluar, name='detail_pengajuan_pindah_keluar'),

    # urls.py
    path('cek-status/', views.cek_status_surat, name='cek_status'),

    path('login/', views.login_view, name='login'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

