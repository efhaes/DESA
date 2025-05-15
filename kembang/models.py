from django.db import models

STATUS_CHOICES = [
    ('diajukan', 'Diajukan'),
    ('diproses', 'Sedang Diproses'),
    ('selesai', 'Sudah Diproses'),
    ('siap', 'Siap Diambil'),
]

class PengajuanSurat(models.Model):
    JENIS_SURAT = [
        ('domisili', 'Surat Domisili'),
        ('sktm', 'Surat Keterangan Tidak Mampu'),
        ('usaha', 'Surat Keterangan Usaha'),
    ]

    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=16)
    alamat = models.CharField(max_length=100)  # <- ini udah bener sekarang
    jenis_surat = models.CharField(max_length=20, choices=JENIS_SURAT)
    keterangan = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='diajukan')
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama} - {self.jenis_surat}"



class AktaKematian(models.Model):
    nama_jenazah = models.CharField(max_length=100)
    nik_jenazah = models.CharField(max_length=16)
    tanggal_kematian = models.DateField()
    tempat_kematian = models.CharField(max_length=100)
    penyebab_kematian = models.CharField(max_length=255, blank=True, null=True)

    nama_pelapor = models.CharField(max_length=100)
    nik_pelapor = models.CharField(max_length=16)
    hubungan_pelapor = models.CharField(max_length=100)

    kk_jenazah = models.FileField(upload_to='akta_kematian/', blank=True, null=True)
    ktp_jenazah = models.FileField(upload_to='akta_kematian/', blank=True, null=True)
    surat_keterangan_kematian = models.FileField(upload_to='akta_kematian/', blank=True, null=True)
    surat_keterangan_rs = models.FileField(upload_to='akta_kematian/', blank=True, null=True)
    dokumen_pendukung_lainnya = models.FileField(upload_to='akta_kematian/', blank=True, null=True)

    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('proses', 'Proses'),
            ('selesai', 'Selesai'),
            ('ditolak', 'Ditolak')
        ],
        default='pending'
    )

    def __str__(self):
        return f"{self.nama_jenazah} - {self.nik_jenazah}"
    
class AktaKelahiran(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=10, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')])
    nama_ayah = models.CharField(max_length=100)
    nama_ibu = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self):
        return f'Akta Kelahiran {self.nama_lengkap}'
