from django.db import models
from django.contrib.auth.models import User

class PengajuanSurat(models.Model):
    JENIS_SURAT = [
        ('domisili', 'Surat Domisili'),
        ('sktm', 'Surat Keterangan Tidak Mampu'),
        ('usaha', 'Surat Keterangan Usaha'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=16)
    jenis_surat = models.CharField(max_length=20, choices=JENIS_SURAT)
    keterangan = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Diproses')

    def __str__(self):
        return f"{self.nama} - {self.jenis_surat}"
