from django.contrib import admin
from .models import PengajuanSurat,AktaKematian,AktaKelahiran,PindahDatang,PindahKeluar,SKTMPengajuan, DomisiliPengajuan,SKUPengajuan

@admin.register(PengajuanSurat)
class PengajuanSuratAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nik', 'jenis_surat','alamat', 'status', 'tanggal','no_whatsapp')
    list_filter = ('status', 'jenis_surat', 'tanggal','alamat')
    search_fields = ('nama', 'alamat')                                    
    ordering = ('-tanggal',)
    


@admin.register(AktaKematian)
class AktaKematianAdmin(admin.ModelAdmin):
    list_display = ('nama_jenazah', 'nik_jenazah', 'tanggal_kematian', 'status', 'tanggal_pengajuan','no_whatsapp')
    search_fields = ('nama_jenazah', 'nik_jenazah')
    list_filter = ('status',)

class AktaKelahiranAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'nama_ayah', 'nama_ibu','no_whatsapp')
    list_filter = ('jenis_kelamin', 'tanggal_lahir')
    search_fields = ('nama_lengkap', 'nama_ayah', 'nama_ibu')

admin.site.register(AktaKelahiran, AktaKelahiranAdmin)

@admin.register(PindahDatang)
class PindahDatangAdmin(admin.ModelAdmin):
    list_display = ('nama', 'asal_daerah', 'tanggal_pindah','no_whatsapp')
    search_fields = ('nama', 'asal_daerah')
    list_filter = ('tanggal_pindah',)


@admin.register(PindahKeluar)
class PindahKeluarAdmin(admin.ModelAdmin):
    list_display = ('nama', 'tujuan_daerah', 'tanggal_pindah','no_whatsapp')
    search_fields = ('nama', 'tujuan_daerah')
    list_filter = ('tanggal_pindah',)




@admin.register(SKTMPengajuan)
class SKTMPengajuanAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'no_whatsapp', 'status', 'tanggal_dibuat')
    list_filter = ('status', 'tanggal_dibuat')
    search_fields = ('nama_lengkap', 'nik', 'no_whatsapp')
    readonly_fields = ('tanggal_dibuat',)

@admin.register(DomisiliPengajuan)
class DomisiliPengajuanAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'no_whatsapp', 'status', 'tanggal_dibuat')
    list_filter = ('status', 'tanggal_dibuat')
    search_fields = ('nama_lengkap', 'nik', 'no_whatsapp')
    readonly_fields = ('tanggal_dibuat',)

@admin.register(SKUPengajuan)
class SKUPengajuanAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'npwp', 'no_whatsapp', 'status', 'tanggal_dibuat')
    list_filter = ('status', 'tanggal_dibuat')
    search_fields = ('nama_lengkap', 'nik', 'npwp', 'no_whatsapp')
    readonly_fields = ('tanggal_dibuat',)
