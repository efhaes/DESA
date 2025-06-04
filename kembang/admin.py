from django.contrib import admin
from .models import AktaKematian,AktaKelahiran,PindahDatang,PindahKeluar,SKTMPengajuan, DomisiliPengajuan,SKUPengajuan,Announcement, AnnouncementImage


    


@admin.register(AktaKematian)
class AktaKematianAdmin(admin.ModelAdmin):
    list_display = ('nama_jenazah', 'nik_jenazah', 'tanggal_kematian', 'status', 'user' ,'tanggal_pengajuan','no_whatsapp')
    search_fields = ('nama_jenazah', 'nik_jenazah')
    list_filter = ('status',)
    readonly_fields = ['tanggal_pengajuan'] 

class AktaKelahiranAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'user' ,'nama_ayah', 'nama_ibu','no_whatsapp')
    list_filter = ('jenis_kelamin', 'tanggal_lahir')
    search_fields = ('nama_lengkap', 'nama_ayah', 'nama_ibu')
    readonly_fields = ['tanggal_pengajuan'] 

admin.site.register(AktaKelahiran, AktaKelahiranAdmin)

@admin.register(PindahDatang)
class PindahDatangAdmin(admin.ModelAdmin):
    list_display = ('nama', 'asal_daerah', 'tanggal_pindah','user' ,'no_whatsapp')
    search_fields = ('nama', 'asal_daerah')
    list_filter = ('tanggal_pindah',)
    readonly_fields = ['tanggal_pengajuan'] 


@admin.register(PindahKeluar)
class PindahKeluarAdmin(admin.ModelAdmin):
    list_display = ('nama', 'tujuan_daerah', 'tanggal_pindah','user' ,'no_whatsapp')
    search_fields = ('nama', 'tujuan_daerah')
    list_filter = ('tanggal_pindah',)
    readonly_fields = ['tanggal_pengajuan'] 




@admin.register(SKTMPengajuan)
class SKTMPengajuanAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'user' ,'no_whatsapp', 'status', 'tanggal_pengajuan')
    list_filter = ('status', 'tanggal_pengajuan')
    search_fields = ('nama_lengkap', 'nik', 'no_whatsapp')
    readonly_fields = ('tanggal_pengajuan',)

@admin.register(DomisiliPengajuan)
class DomisiliPengajuanAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'user' ,'no_whatsapp', 'status', 'tanggal_pengajuan')
    list_filter = ('status', 'tanggal_pengajuan')
    search_fields = ('nama_lengkap', 'nik', 'no_whatsapp')
    readonly_fields = ('tanggal_pengajuan',)

@admin.register(SKUPengajuan)
class SKUPengajuanAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'user' ,'npwp', 'no_whatsapp', 'status', 'tanggal_pengajuan')
    list_filter = ('status', 'tanggal_pengajuan')
    search_fields = ('nama_lengkap', 'nik', 'npwp', 'no_whatsapp')
    readonly_fields = ('tanggal_pengajuan',)


class AnnouncementImageInline(admin.TabularInline):  # atau bisa pakai StackedInline
    model = AnnouncementImage
    extra = 1  # jumlah form kosong tambahan yang ditampilkan

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'is_active')
    list_filter = ('is_active', 'published_at')
    search_fields = ('title', 'content')
    inlines = [AnnouncementImageInline]

admin.site.register(Announcement, AnnouncementAdmin)