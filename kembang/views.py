from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PengajuanSurat,AktaKematian,AktaKelahiran,PindahDatang,PindahKeluar
from .forms import PengajuanSuratForm,AktaKematianForm,AktaKelahiranForm,PindahDatangForm,PindahKeluarForm,AktaKematianHasilForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q

def status_surat(request):
    nama = request.GET.get('nama')
    hasil = None

    if nama:
        hasil = PengajuanSurat.objects.filter(nama__icontains=nama).order_by('-tanggal')

    return render(request, 'surat/status.html', {'hasil': hasil, 'nama': nama})


def home(request):
    return render(request, 'profile/home.html')

def tentang(request):
    return render(request, 'profile/tentang.html')

def profil(request):
    return render(request, 'profile/profil.html')


def ajukan_surat(request):
    if request.method == 'POST':
        form = PengajuanSuratForm(request.POST)
        if form.is_valid():
            surat = form.save(commit=False)
            surat.user = request.user
            surat.save()
            return redirect('status')
    else:
        form = PengajuanSuratForm()
    return render(request, 'surat/ajukan.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('semua_pengajuan')  # langsung ke dashboard kalau udah login

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:  # hanya staff yang boleh login ke admin
                login(request, user)
                return redirect('semua_pengajuan')
            else:
                messages.error(request, "Akses ditolak: hanya admin yang bisa login.")
        else:
            messages.error(request, "Username atau password salah.")
    else:
        form = AuthenticationForm()

    return render(request, 'surat/login.html', {'form': form})


def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def semua_pengajuan(request):
    akta_kelahiran = AktaKelahiran.objects.all().order_by('-tanggal_lahir')
    pindah_datang = PindahDatang.objects.all().order_by('-tanggal_pindah')
    pindah_keluar = PindahKeluar.objects.all().order_by('-tanggal_pindah')
    return render(request, 'admin/dashboard.html', {
        'akta_kelahiran': akta_kelahiran,
        'pindah_datang': pindah_datang,
        'pindah_keluar': pindah_keluar,
    })


@login_required
def pengajuan_akta_kematian(request):
    if request.method == 'POST':
        form = AktaKematianForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('riwayat_kematian')  # ganti sesuai nama URL beranda kamu
    else:
        form = AktaKematianForm()
    return render(request, 'surat/aktakematianform.html', {'form': form})

@staff_member_required
def daftar_pengajuan_akta_kematian(request):
    pengajuan = AktaKematian.objects.all().order_by('-tanggal_pengajuan')
    return render(request, 'admin/daftar_kematian.html', {'pengajuan': pengajuan})

@staff_member_required
def detail_pengajuan_akta_kematian(request, pk):
    akta = get_object_or_404(AktaKematian, pk=pk)

    if request.method == 'POST':
        status = request.POST.get('status')
        hasil_surat = request.FILES.get('hasil_surat')
        akta.status = status
        if hasil_surat:
            akta.hasil_surat = hasil_surat
        akta.save()
        messages.success(request, "Status berhasil diperbarui.")
        return redirect('daftar_pengajuan_akta_kematian') 

    return render(request, 'admin/detail_kematian.html', {'akta': akta})


@login_required
def pengajuan_akta_kelahiran(request):
    if request.method == 'POST':
        form = AktaKelahiranForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('home')
    else:
        form = AktaKelahiranForm()
    return render(request, 'surat/akta_kelahiran_form.html', {'form': form})


@staff_member_required
def daftar_pengajuan_kelahiran(request):
    pengajuan = AktaKelahiran.objects.all().order_by('-tanggal_lahir')
    return render(request, 'admin/daftarkelahiran.html', {'pengajuan': pengajuan})

@staff_member_required
def detail_pengajuan_kelahiran(request, pk):
    akta = get_object_or_404(AktaKelahiran, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        hasil_surat = request.FILES.get('hasil_surat')
        akta.status = status
        if hasil_surat:
            akta.hasil_surat = hasil_surat
        akta.save()
        messages.success(request, "Status berhasil diperbarui.")
        return redirect('detail_pengajuan_kelahiran', pk=pk)
    return render(request, 'admin/detail_kelahiran.html', {'akta': akta})

@login_required
def pengajuan_pindah_datang(request):
    if request.method == 'POST':
        form = AktaKelahiranForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('home')
    else:
        form = AktaKelahiranForm()
    return render(request, 'admin/aktakelahiran.html', {'form': form})


@staff_member_required
def daftar_pindah_datang(request):
    pengajuan = AktaKelahiran.objects.all().order_by('-tanggal_lahir')
    return render(request, 'admin/akta_kelahiran.html', {'pengajuan': pengajuan})

@staff_member_required
def detail_pindah_datang(request, pk):
    akta = get_object_or_404(AktaKelahiran, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        hasil_surat = request.FILES.get('hasil_surat')
        akta.status = status
        if hasil_surat:
            akta.hasil_surat = hasil_surat
        akta.save()
        messages.success(request, "Status berhasil diperbarui.")
        return redirect('detail_pengajuan_kelahiran', pk=pk)
    return render(request, 'admin/detail_kelahiran.html', {'akta': akta})



@login_required
def pengajuan_pindah_keluar(request):
    if request.method == 'POST':
        form = AktaKelahiranForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('home')
    else:
        form = AktaKelahiranForm()
    return render(request, 'admin/aktakelahiran.html', {'form': form})


@staff_member_required
def daftar_pindah_keluar(request):
    pengajuan = AktaKelahiran.objects.all().order_by('-tanggal_lahir')
    return render(request, 'admin/akta_kelahiran.html', {'pengajuan': pengajuan})

@staff_member_required
def detail_pindah_keluar(request, pk):
    akta = get_object_or_404(AktaKelahiran, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        hasil_surat = request.FILES.get('hasil_surat')
        akta.status = status
        if hasil_surat:
            akta.hasil_surat = hasil_surat
        akta.save()
        messages.success(request, "Status berhasil diperbarui.")
        return redirect('detail_pengajuan_kelahiran', pk=pk)
    return render(request, 'admin/detail_kelahiran.html', {'akta': akta})





@login_required
def cek_status_surat(request):
    hasil = None
    jenis = request.GET.get('jenis')
    nik = request.GET.get('nik')

    if jenis and nik:
        if jenis == 'kelahiran':
            hasil = AktaKelahiran.objects.filter(Q(nama_lengkap__icontains=nik) | Q(no_whatsapp__icontains=nik))
        elif jenis == 'kematian':
            hasil = AktaKematian.objects.filter(Q(nama_jenazah__icontains=nik) | Q(no_whatsapp__icontains=nik))
        elif jenis == 'pindah_datang':
            hasil = PindahDatang.objects.filter(Q(nama__icontains=nik) | Q(nik__icontains=nik))
        elif jenis == 'pindah_keluar':
            hasil = PindahKeluar.objects.filter(Q(nama__icontains=nik) | Q(nik__icontains=nik))

    return render(request, 'profile/cek_status.html', {
        'hasil': hasil,
        'jenis': jenis,
        'nik': nik
    })

