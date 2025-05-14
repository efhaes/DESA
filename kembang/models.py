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
