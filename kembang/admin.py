from django.contrib import admin
from .models import PengajuanSurat

@admin.register(PengajuanSurat)
class PengajuanSuratAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nik', 'jenis_surat', 'tanggal_pengajuan', 'status')
    list_filter = ('jenis_surat', 'status', 'tanggal_pengajuan')
    search_fields = ('nama', 'nik')
    ordering = ('-tanggal_pengajuan',)
