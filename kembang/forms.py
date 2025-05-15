from django import forms
from .models import PengajuanSurat,AktaKematian,AktaKelahiran,PindahDatang, PindahKeluar

 

class PengajuanSuratForm(forms.ModelForm):
    class Meta:
        model = PengajuanSurat
        fields = ['nama', 'nik', 'alamat', 'jenis_surat','no_whatsapp','keterangan']

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = PengajuanSurat
        fields = ['status']
        

class AktaKematianForm(forms.ModelForm):
    class Meta:
        model = AktaKematian
        fields = [
            'nama_jenazah',
            'nik_jenazah',
            'tanggal_kematian',
            'tempat_kematian',
            'penyebab_kematian',
            'nama_pelapor',
            'nik_pelapor',
            'hubungan_pelapor',
            'no_whatsapp',
            'kk_jenazah',
            'ktp_jenazah',
            'surat_keterangan_kematian',
            'surat_keterangan_rs',
            'dokumen_pendukung_lainnya',
        ]
        widgets = {
            'tanggal_kematian': forms.DateInput(attrs={'type': 'date'}),
            'penyebab_kematian': forms.TextInput(attrs={'placeholder': 'Misal: Sakit, Kecelakaan, dll'}),
        }
        labels = {
            'kk_jenazah': 'Upload KK Jenazah',
            'ktp_jenazah': 'Upload KTP Jenazah',
            'surat_keterangan_kematian': 'Surat Keterangan Kematian dari RT/RW',
            'surat_keterangan_rs': 'Surat Keterangan RS (jika ada)',
            'dokumen_pendukung_lainnya': 'Dokumen Pendukung Lainnya (Opsional)',
        }

class AktaKelahiranForm(forms.ModelForm):
    class Meta:
        model = AktaKelahiran
        fields = [
            'nama_lengkap',
            'tempat_lahir',
            'tanggal_lahir',
            'jenis_kelamin',
            'nama_ayah',
            'nama_ibu',
            'alamat',
            'no_whatsapp',
        ]
        widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
            'alamat': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'no_whatsapp': 'Nomor WhatsApp Aktif',
        }




class PindahDatangForm(forms.ModelForm):
    class Meta:
        model = PindahDatang
        exclude = ['status', 'hasil_surat']  # status dan hasil_surat hanya untuk admin
        widgets = {
            'tanggal_pindah': forms.DateInput(attrs={'type': 'date'}),
            'alasan_pindah': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'nama': 'Nama Lengkap',
            'nik': 'NIK',
            'asal_daerah': 'Asal Daerah',
            'tujuan_daerah': 'Tujuan Daerah',
            'tanggal_pindah': 'Tanggal Pindah',
            'alasan_pindah': 'Alasan Pindah',
            'kk_lama': 'Upload KK Lama',
            'ktp': 'Upload KTP',
            'surat_pengantar': 'Surat Pengantar RT/RW',
            'no_whatsapp': 'Nomor WhatsApp Aktif',
        }

class PindahKeluarForm(forms.ModelForm):
    class Meta:
        model = PindahKeluar
        fields = [
            'nama',
            'nik',
            'asal_daerah',
            'tujuan_daerah',
            'tanggal_pindah',
            'alasan_pindah',
            'kk',
            'ktp',
            'surat_pengantar',
            'no_whatsapp',
        ]
        widgets = {
            'tanggal_pindah': forms.DateInput(attrs={'type': 'date'}),
            'alasan_pindah': forms.Textarea(attrs={'rows': 3}),
            'no_whatsapp': forms.TextInput(attrs={'placeholder': '08xxxxxxxxxx'}),
        }
        
class AktaKematianHasilForm(forms.ModelForm):
    class Meta:
        model = AktaKematian
        fields = ['status', 'hasil_surat'] 
