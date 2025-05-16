from django import forms
from .models import PengajuanSurat,AktaKematian,AktaKelahiran,PindahDatang, PindahKeluar,SKTMPengajuan, DomisiliPengajuan, SKUPengajuan

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
        



class SKTMPengajuanForm(forms.ModelForm):
    class Meta:
        model = SKTMPengajuan
        fields = [
            'nama_lengkap',
            'nik',
            'no_whatsapp',
            'surat_pengantar',
            'foto_ktp',
            'foto_kk',
            'surat_pernyataan'
        ]
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
            'nik': forms.TextInput(attrs={'class': 'form-control'}),
            'no_whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'surat_pengantar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_ktp': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_kk': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'surat_pernyataan': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class DomisiliPengajuanForm(forms.ModelForm):
    class Meta:
        model = DomisiliPengajuan
        fields = [
            'nama_lengkap',
            'nik',
            'no_whatsapp',
            'surat_pengantar',
            'foto_ktp',
            'foto_kk',
            'surat_permohonan'
        ]
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
            'nik': forms.TextInput(attrs={'class': 'form-control'}),
            'no_whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'surat_pengantar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_ktp': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_kk': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'surat_permohonan': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class SKUPengajuanForm(forms.ModelForm):
    class Meta:
        model = SKUPengajuan
        fields = [
            'nama_lengkap',
            'nik',
            'no_whatsapp',
            'npwp',
            'surat_pengantar',
            'surat_permohonan',
            'foto_ktp',
            'foto_kk',
            'surat_kuasa'
        ]
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
            'nik': forms.TextInput(attrs={'class': 'form-control'}),
            'no_whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'npwp': forms.TextInput(attrs={'class': 'form-control'}),
            'surat_pengantar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'surat_permohonan': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_ktp': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_kk': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
        }




class RegisterForm(forms.Form):
    nik = forms.CharField(max_length=16, label='NIK')
    nama = forms.CharField(max_length=100, label='Nama Lengkap')
    alamat = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='Alamat')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Konfirmasi Password')

    def clean_nik(self):
        nik = self.cleaned_data['nik']
        if User.objects.filter(username=nik).exists():
            raise ValidationError("NIK sudah terdaftar.")
        return nik

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Password tidak cocok.")


