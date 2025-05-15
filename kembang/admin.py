from django.contrib import admin
from .models import PengajuanSurat,AktaKematian,AktaKelahiran,PindahDatang,PindahKeluar

@admin.register(PengajuanSurat)
class PengajuanSuratAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nik', 'jenis_surat','alamat', 'status', 'tanggal')
    list_filter = ('status', 'jenis_surat', 'tanggal','alamat')
    search_fields = ('nama', 'alamat')                                    
    ordering = ('-tanggal',)
    


@admin.register(AktaKematian)
class AktaKematianAdmin(admin.ModelAdmin):
    list_display = ('nama_jenazah', 'nik_jenazah', 'tanggal_kematian', 'status', 'tanggal_pengajuan')
    search_fields = ('nama_jenazah', 'nik_jenazah')
    list_filter = ('status',)

class AktaKelahiranAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'nama_ayah', 'nama_ibu')
    list_filter = ('jenis_kelamin', 'tanggal_lahir')
    search_fields = ('nama_lengkap', 'nama_ayah', 'nama_ibu')

admin.site.register(AktaKelahiran, AktaKelahiranAdmin)

@admin.register(PindahDatang)
class PindahDatangAdmin(admin.ModelAdmin):
    list_display = ('nama', 'asal', 'tanggal_datang')
    search_fields = ('nama', 'asal')
    list_filter = ('tanggal_datang',)

@admin.register(PindahKeluar)
class PindahKeluarAdmin(admin.ModelAdmin):
    list_display = ('nama', 'tujuan', 'tanggal_pindah')
    search_fields = ('nama', 'tujuan')
    list_filter = ('tanggal_pindah',)

