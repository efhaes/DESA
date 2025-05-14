from django.contrib import admin
from .models import PengajuanSurat

class PengajuanSuratAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis_surat', 'status', 'tanggal')  
    list_filter = ('jenis_surat', 'status', 'tanggal')           
    ordering = ['tanggal']                                      

admin.site.register(PengajuanSurat, PengajuanSuratAdmin)
