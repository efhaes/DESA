from django import forms
from .models import PengajuanSurat

class PengajuanSuratForm(forms.ModelForm):
    class Meta:
        model = PengajuanSurat
        fields = ['nama', 'nik', 'alamat', 'jenis_surat', 'keterangan']

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = PengajuanSurat
        fields = ['status']
