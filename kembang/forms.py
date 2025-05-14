# pelayanan/forms.py
from django import forms
from .models import PengajuanSurat

class PengajuanSuratForm(forms.ModelForm):
    class Meta:
        model = PengajuanSurat
        fields = ['nama', 'nik', 'jenis_surat']
