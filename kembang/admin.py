from django.contrib import admin
from .models import PengajuanSurat

@admin.register(PengajuanSurat)
class PengajuanSuratAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nik', 'jenis_surat','alamat', 'status', 'tanggal')
    list_filter = ('status', 'jenis_surat', 'tanggal','alamat')
    search_fields = ('nama', 'alamat')                                    
    ordering = ('-tanggal',)

