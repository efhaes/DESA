from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PengajuanSurat
from .forms import PengajuanSuratForm
from django.contrib.auth import authenticate, login
from .forms import UpdateStatusForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


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
    semua_surat = PengajuanSurat.objects.all().order_by('-tanggal')
    return render(request, 'admin/dashboard.html', {'semua_surat': semua_surat})


@user_passes_test(is_admin)
def update_status(request, surat_id):
    surat = get_object_or_404(PengajuanSurat, id=surat_id)
    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=surat)
        if form.is_valid():
            form.save()
            return redirect('semua_pengajuan')
    else:
        form = UpdateStatusForm(instance=surat)
    return render(request, 'admin/update_status.html', {'form': form})