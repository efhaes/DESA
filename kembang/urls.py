# pelayanan/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    
    path('tentang/', views.tentang, name='tentang'),
    path('profil/', views.profil, name='profil'),
    path('persyaratan/', views.persyaratan, name='persyaratan'),
    

    path('semua/', views.semua_pengajuan, name='semua_pengajuan'),
    
    path('pengajuan-akta-kematian/', views.pengajuan_akta_kematian, name='pengajuan_akta_kematian'),
    path('kematian/akta-kematian/', views.daftar_pengajuan_akta_kematian, name='daftar_pengajuan_akta_kematian'),
    path('kematian/akta-kematian/<int:pk>/', views.detail_pengajuan_akta_kematian, name='detail_pengajuan_akta_kematian'),
    # Akta Kelahiran
    path('pengajuan/akta-kelahiran/', views.pengajuan_akta_kelahiran, name='pengajuan_akta_kelahiran'),
    path('kelahiran/akta-kelahiran/', views.daftar_pengajuan_kelahiran, name='daftar_pengajuan_kelahiran'),
    path('kelahiran/akta-kelahiran/<int:pk>/', views.detail_pengajuan_kelahiran, name='detail_pengajuan_kelahiran'),

    # Pindah Datang
    path('pengajuan/pindah-datang/', views.pengajuan_pindah_datang, name='pengajuan_pindah_datang'),
    path('datang/pindah-datang/', views.daftar_pindah_datang, name='daftar_pengajuan_pindah_datang'),
    path('datang/pindah-datang/<int:pk>/', views.detail_pindah_datang, name='detail_pengajuan_pindah_datang'),

    # Pindah Keluar
    path('pengajuan/pindah-keluar/', views.pengajuan_pindah_keluar, name='pengajuan_pindah_keluar'),
    path('keluar/pindah-keluar/', views.daftar_pindah_keluar, name='daftar_pengajuan_pindah_keluar'),
    path('keluar/pindah-keluar/<int:pk>/', views.detail_pindah_keluar, name='detail_pengajuan_pindah_keluar'),
    
    # sktm
    path('pengajuan/sktm/', views.pengajuan_sktm, name='pengajuan_sktm'),
    path('sktm/sktm/', views.daftar_sktm, name='daftar_pengajuan_sktm'),
    path('sktm/sktm/<int:pk>/', views.detail_sktm, name='detail_pengajuan_sktm'),
    
    # domisili
    path('domisili/pengajuan/', views.pengajuan_domisili, name='pengajuan_domisili'),
    path('domisili/daftar/', views.daftar_domisili, name='daftar_domisili'),
    path('domisili/<int:pk>/', views.detail_domisili, name='detail_pengajuan_domisili'),
    
    # sku
    path('sku/pengajuan/', views.pengajuan_sku, name='pengajuan_sku'),
    path('sku/daftar/', views.daftar_sku, name='daftar_sku'),
    path('sku/<int:pk>/', views.detail_sku, name='detail_pengajuan_sku'),

    # urls.py
    path('cek-status/', views.cek_status_surat, name='cek_status'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('kelola/pengumuman/', views.announcement_manage, name='announcement_manage'),
    path('pengumuman/', views.announcement_list, name='announcement_list'),
    path('pengumuman/<int:pk>/', views.announcement_detail, name='announcement_detail'),
    path('pengajuan/semua-pengajuan/', views.semua_pengajuan, name='semua_pengajuan'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

