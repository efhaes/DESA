from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES = [
    ('diajukan', 'Diajukan'),
    ('diproses', 'Sedang Diproses'),
    ('selesai', 'Sudah Diproses'),
    

]


class AktaKematian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    nama_jenazah = models.CharField(max_length=100)
    nik_jenazah = models.CharField(max_length=16)
    tanggal_kematian = models.DateField()
    tempat_kematian = models.CharField(max_length=100)
    penyebab_kematian = models.CharField(max_length=255, blank=True, null=True)

    nama_pelapor = models.CharField(max_length=100)
    nik_pelapor = models.CharField(max_length=16)
    hubungan_pelapor = models.CharField(max_length=100)
    no_whatsapp = models.CharField(max_length=15, verbose_name="No. WhatsApp")  # tambahkan ini
    kk_jenazah = models.FileField(upload_to='akta_kematian/', blank=True, null=True)
    ktp_jenazah = models.FileField(upload_to='akta_kematian/', blank=True, null=True)
    surat_keterangan_kematian = models.FileField(upload_to='akta_kematian/', blank=True, null=True)
    surat_keterangan_rs = models.FileField(upload_to='akta_kematian/', blank=True, null=True)
    dokumen_pendukung_lainnya = models.FileField(upload_to='akta_kematian/', blank=True, null=True)

    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='diajukan')
    hasil_surat = models.FileField(upload_to='hasil_surat/akta_kematian/', blank=True, null=True)

    def __str__(self):
        return f"{self.nama_jenazah} - {self.nik_jenazah}"
    
class AktaKelahiran(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=10, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')])
    nama_ayah = models.CharField(max_length=100)
    nama_ibu = models.CharField(max_length=100)
    alamat = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='diajukan')
    no_whatsapp = models.CharField(max_length=15, verbose_name="No. WhatsApp") 
    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    hasil_surat = models.FileField(upload_to='hasil_surat/akta_kelahiran/', blank=True, null=True)

    def __str__(self):
        return f'Akta Kelahiran {self.nama_lengkap}'


class PindahKeluar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=16)
    asal_daerah = models.CharField(max_length=100)
    tujuan_daerah = models.CharField(max_length=100)
    tanggal_pindah = models.DateField()
    alasan_pindah = models.TextField()
    kk = models.FileField(upload_to='pindah_keluar/kk/')
    ktp = models.FileField(upload_to='pindah_keluar/ktp/')
    surat_pengantar = models.FileField(upload_to='pindah_keluar/surat_pengantar/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='diajukan')
    no_whatsapp = models.CharField(max_length=15, verbose_name="No. WhatsApp")
    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    hasil_surat = models.FileField(upload_to='hasil_surat/akta_kematian/', blank=True, null=True)

    def __str__(self):
        return f"Pindah Keluar - {self.nama} ({self.nik})"



class PindahDatang(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=16)
    asal_daerah = models.CharField(max_length=100)
    tujuan_daerah = models.CharField(max_length=100)
    tanggal_pindah = models.DateField()
    alasan_pindah = models.TextField()
    kk_lama = models.FileField(upload_to='pindah_datang/kk_lama/')
    ktp = models.FileField(upload_to='pindah_datang/ktp/')
    surat_pengantar = models.FileField(upload_to='pindah_datang/surat_pengantar/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='diajukan')
    no_whatsapp = models.CharField(max_length=15, verbose_name="No. WhatsApp")  # tambahkan ini
    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    hasil_surat = models.FileField(upload_to='hasil_surat/akta_kematian/', blank=True, null=True)

    def __str__(self):
        return f"Pindah Datang - {self.nama} ({self.nik})"



class SKTMPengajuan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    nik = models.CharField(max_length=16)
    no_whatsapp = models.CharField(max_length=15)

    surat_pengantar = models.FileField(upload_to='sktm/surat_pengantar/')
    foto_ktp = models.ImageField(upload_to='sktm/foto_ktp/')
    foto_kk = models.ImageField(upload_to='sktm/foto_kk/')
    surat_pernyataan = models.FileField(upload_to='sktm/surat_pernyataan/')
    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='diajukan')
    hasil_surat = models.FileField(upload_to='sktm/hasil_surat/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.nama_lengkap} - {self.nik}"
    
class DomisiliPengajuan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    nik = models.CharField(max_length=16)
    no_whatsapp = models.CharField(max_length=15)

    surat_pengantar = models.FileField(upload_to='domisili/surat_pengantar/')
    foto_ktp = models.ImageField(upload_to='domisili/foto_ktp/')
    foto_kk = models.ImageField(upload_to='domisili/foto_kk/')
    surat_permohonan = models.FileField(upload_to='domisili/surat_permohonan/')
    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='diajukan')
    hasil_surat = models.FileField(upload_to='domisili/hasil_surat/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.nama_lengkap} - {self.nik}"

class SKUPengajuan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    nik = models.CharField(max_length=16)
    no_whatsapp = models.CharField(max_length=15)
    npwp = models.CharField(max_length=50)
    surat_pengantar = models.FileField(upload_to='SKU/surat_pengantar/')
    surat_permohonan = models.FileField(upload_to='SKU/surat_permohonan/')
    foto_ktp = models.ImageField(upload_to='SKU/foto_ktp/')
    foto_kk = models.ImageField(upload_to='SKU/foto_kk/')
    surat_kuasa = models.ImageField(upload_to='SKU/surat_kuasa/',blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='diajukan')
    hasil_surat = models.FileField(upload_to='SKU/hasil_surat/', blank=True, null=True)
    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama_lengkap} - {self.nik}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self):
        return self.nama
    
from django.db import models
class Announcement(models.Model):
    title = models.CharField(max_length=200)             
    content = models.TextField()                          
    published_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)        
    is_active = models.BooleanField(default=True)           

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']   # pengumuman terbaru muncul paling atas
        verbose_name = "Pengumuman"
        verbose_name_plural = "Pengumuman"


class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='announcement_images/')

    def __str__(self):
        return f"Gambar untuk {self.announcement.title}"
