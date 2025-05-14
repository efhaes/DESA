# pelayanan/views.py
from django.contrib.auth.decorators import login_required
from .models import PengajuanSurat
from .forms import PengajuanSuratForm
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('riwayat_surat')  # Sudah login, langsung ke dashboard

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('riwayat_surat')  # Ganti dengan halaman tujuanmu
        else:
            messages.error(request, 'Username atau password salah!')

    return render(request, 'pelayanan/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def ajukan_surat(request):
    if request.method == 'POST':
        form = PengajuanSuratForm(request.POST)
        if form.is_valid():
            surat = form.save(commit=False)
            surat.user = request.user
            surat.save()
            return render(request, 'pelayanan/sukses.html')
    else:
        form = PengajuanSuratForm()
    return render(request, 'pelayanan/ajukan_surat.html', {'form': form})

@login_required
def riwayat_surat(request):
    surat_user = PengajuanSurat.objects.filter(user=request.user)
    return render(request, 'pelayanan/riwayat.html', {'surat_list': surat_user})

@staff_member_required
def semua_pengajuan(request):
    semua = PengajuanSurat.objects.all()
    return render(request, 'pelayanan/semua_pengajuan.html', {'surat_list': semua})
