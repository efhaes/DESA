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
            'kk_jenazah',
            'ktp_jenazah',
            'surat_keterangan_kematian',
            'surat_keterangan_rs',
            'dokumen_pendukung_lainnya',
        ]
        widgets = {
            'tanggal_kematian': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'nama_jenazah': 'Nama Jenazah',
            'nik_jenazah': 'NIK Jenazah',
            'tanggal_kematian': 'Tanggal Kematian',
            'tempat_kematian': 'Tempat Kematian',
            'penyebab_kematian': 'Penyebab Kematian',
            'nama_pelapor': 'Nama Pelapor',
            'nik_pelapor': 'NIK Pelapor',
            'hubungan_pelapor': 'Hubungan dengan Jenazah',
            'kk_jenazah': 'Upload KK Jenazah',
            'ktp_jenazah': 'Upload KTP Jenazah',
            'surat_keterangan_kematian': 'Surat Keterangan Kematian (Desa)',
            'surat_keterangan_rs': 'Surat Keterangan Rumah Sakit',
            'dokumen_pendukung_lainnya': 'Dokumen Pendukung Lainnya (Opsional)',
        }
        
class AktaKelahiranForm(forms.ModelForm):
    class Meta:
        model = AktaKelahiran
        fields = ['nama_lengkap', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'nama_ayah', 'nama_ibu', 'alamat','no_whatsapp']
        widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
            'alamat': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }




class PindahDatangForm(forms.ModelForm):
    class Meta:
        model = PindahDatang
        fields = '__all__'
        widgets = {
            'tanggal_pindah': forms.DateInput(attrs={'type': 'date'}),
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
        }

class PindahKeluarForm(forms.ModelForm):
    class Meta:
        model = PindahKeluar
        fields = '__all__'
        widgets = {
            'tanggal_pindah': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'nama': 'Nama Lengkap',
            'nik': 'NIK',
            'asal_daerah': 'Asal Daerah',
            'tujuan_daerah': 'Tujuan Daerah',
            'tanggal_pindah': 'Tanggal Pindah',
            'alasan_pindah': 'Alasan Pindah',
            'kk': 'Upload KK',
            'ktp': 'Upload KTP',
            'surat_pengantar': 'Surat Pengantar RT/RW',
        }
