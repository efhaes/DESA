from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PengajuanSurat
from .forms import PengajuanSuratForm
from django.contrib.auth import authenticate, login

@login_required
def ajukan_surat(request):
    if request.method == 'POST':
        form = PengajuanSuratForm(request.POST)
        if form.is_valid():
            surat = form.save(commit=False)
            surat.user = request.user
            surat.save()
            return redirect('status_surat')
    else:
        form = PengajuanSuratForm()
    return render(request, 'surat/ajukan.html', {'form': form})

@login_required
def status_surat(request):
    daftar = PengajuanSurat.objects.filter(user=request.user)
    return render(request, 'surat/status.html', {'daftar': daftar})

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def semua_pengajuan(request):
    daftar = PengajuanSurat.objects.all()
    return render(request, 'surat/semua_pengajuan.html', {'daftar': daftar})


def home(request):
    return render(request, 'profile/home.html')

def tentang(request):
    return render(request, 'profile/tentang.html')

def profil(request):
    return render(request, 'profile/profil.html')

@login_required
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

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'surat/login.html', {'error': 'Username atau password salah'})
    return render(request, 'surat/login.html')