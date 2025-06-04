from django import forms
from .models import AktaKematian, AktaKelahiran, PindahDatang, PindahKeluar, SKTMPengajuan, DomisiliPengajuan, SKUPengajuan, Announcement,AnnouncementImage
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AktaKematianForm(forms.ModelForm):
    class Meta:
        model = AktaKematian
        exclude = ['user', 'status', 'hasil_surat', 'tanggal_pengajuan']
        widgets = {
            'tanggal_kematian': forms.DateInput(attrs={'type': 'date'}),
        }


class AktaKelahiranForm(forms.ModelForm):
    class Meta:
        model = AktaKelahiran
        exclude = ['user', 'status', 'hasil_surat', 'tanggal_pengajuan']
        widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
            'alamat': forms.Textarea(attrs={'rows': 2}),
        }


class PindahDatangForm(forms.ModelForm):
    class Meta:
        model = PindahDatang
        exclude = ['user', 'status', 'hasil_surat', 'tanggal_pengajuan']
        widgets = {
            'tanggal_pindah': forms.DateInput(attrs={'type': 'date'}),
            'alasan_pindah': forms.Textarea(attrs={'rows': 2}),
        }


class PindahKeluarForm(forms.ModelForm):
    class Meta:
        model = PindahKeluar
        exclude = ['user', 'status', 'hasil_surat', 'tanggal_pengajuan']
        widgets = {
            'tanggal_pindah': forms.DateInput(attrs={'type': 'date'}),
            'alasan_pindah': forms.Textarea(attrs={'rows': 2}),
        }

    def clean_no_whatsapp(self):
        no = self.cleaned_data.get('no_whatsapp', '').replace('+', '').replace(' ', '').replace('-', '')
        if no.startswith('0'):
            no = '62' + no[1:]
        elif not no.startswith('62'):
            raise forms.ValidationError("Nomor WhatsApp harus diawali dengan 62 atau 0.")
        return no


class SKTMPengajuanForm(forms.ModelForm):
    class Meta:
        model = SKTMPengajuan
        exclude = ['user', 'status', 'hasil_surat', 'tanggal_pengajuan']


class DomisiliPengajuanForm(forms.ModelForm):
    class Meta:
        model = DomisiliPengajuan
        exclude = ['user', 'status', 'hasil_surat', 'tanggal_pengajuan']


class SKUPengajuanForm(forms.ModelForm):
    class Meta:
        model = SKUPengajuan
        exclude = ['user', 'status', 'hasil_surat', 'tanggal_pengajuan']


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

from django import forms
from .models import Announcement, AnnouncementImage
from django.forms import modelformset_factory

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'is_active']

class AnnouncementImageForm(forms.ModelForm):
    class Meta:
        model = AnnouncementImage
        fields = ['image']

# Formset untuk banyak gambar dalam satu pengumuman
AnnouncementImageFormSet = modelformset_factory(
    AnnouncementImage,
    form=AnnouncementImageForm,
    extra=3,  # bisa diatur sesuai kebutuhan
    can_delete=True
)


