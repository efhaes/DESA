from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PengajuanSurat,AktaKematian,AktaKelahiran,PindahDatang,PindahKeluar,UserProfile,SKTMPengajuan
from .forms import PengajuanSuratForm,AktaKematianForm,AktaKelahiranForm,PindahDatangForm,PindahKeluarForm,SKUPengajuanForm
from .models import DomisiliPengajuan,SKUPengajuan
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegisterForm,SKTMPengajuanForm,DomisiliPengajuanForm
from django.db.models import Q
from itertools import chain 

def status_surat(request):
    nama = request.GET.get('nama')
    hasil = None

    if nama:
        hasil = PengajuanSurat.objects.filter(nama__icontains=nama).order_by('-tanggal')

    return render(request, 'surat/status.html', {'hasil': hasil, 'nama': nama})


def home(request):
    return render(request, 'profile/home.html')
def persyaratan(request):
    return render(request, 'profile/persyaratan.html')

def logout_view(request):
    logout(request)
    return redirect('home')

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
    if request.method == 'POST':
        nik = request.POST.get('nik')
        password = request.POST.get('password')
        user = authenticate(request, username=nik, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')  # Redirect ke admin site Django
            else:
                return redirect('home')  # Ganti dengan URL masyarakat/home
        else:
            messages.error(request, 'NIK atau password salah')
            return redirect('login')
    return render(request, 'surat/login.html')


def is_admin(user):
    return user.is_staff

@staff_member_required
def semua_pengajuan(request):
    akta_kelahiran = AktaKelahiran.objects.all()
    pindah_datang = PindahDatang.objects.all()
    pindah_keluar = PindahKeluar.objects.all()
    akta_kematian = AktaKematian.objects.all()

    return render(request, 'admin/dashboard.html', {
        'akta_kelahiran': akta_kelahiran,
        'pindah_datang': pindah_datang,
        'pindah_keluar': pindah_keluar,
        'akta_kematian': akta_kematian,
    })


@login_required
def pengajuan_akta_kematian(request):
    if request.method == 'POST':
        form = AktaKematianForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('pengajuan_akta_kematian')  # Bisa diarahkan ke halaman status atau beranda
    else:
        form = AktaKematianForm()
    return render(request, 'surat/aktakematian_form.html', {'form': form})

@staff_member_required
def daftar_pengajuan_akta_kematian(request):
    daftar = AktaKematian.objects.all().order_by('-tanggal_pengajuan')
    context = {'daftar': daftar}
    return render(request, 'admin/daftar_kematian.html', context)

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
        return redirect('detail_pengajuan_akta_kematian',pk=pk)

    return render(request, 'admin/akta_kematian_detail.html', {'akta': akta})



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
    context = {'pengajuan': pengajuan}
    return render(request, 'admin/daftar_kelahiran.html', context)



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
        form = PindahDatangForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('home')
    else:
        form = PindahDatangForm()
    return render(request, 'surat/datang_form.html', {'form': form})


@staff_member_required
def daftar_pindah_datang(request):
    pengajuan = PindahDatang.objects.all().order_by('-tanggal_pindah')
    return render(request, 'admin/daftar_datang.html', {'pengajuan': pengajuan})



@staff_member_required
def detail_pindah_datang(request, pk):
    datang = get_object_or_404(PindahDatang, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        hasil_surat = request.FILES.get('hasil_surat')
        datang.status = status
        if hasil_surat:
            datang.hasil_surat = hasil_surat
        datang.save()
        messages.success(request, "Status berhasil diperbarui.")
        return redirect('detail_pengajuan_pindah_datang', pk=pk)
    return render(request, 'admin/detail_datang.html', {'datang': datang})



@login_required
def pengajuan_pindah_keluar(request):
    if request.method == 'POST':
        form = PindahKeluarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('home')
    else:
        form = PindahKeluarForm()
    return render(request, 'surat/keluar_form.html', {'form': form})


@staff_member_required
def daftar_pindah_keluar(request):
    pengajuan = PindahKeluar.objects.all().order_by('-tanggal_pindah')
    return render(request, 'admin/daftar_keluar.html', {'pengajuan': pengajuan})

@staff_member_required
def detail_pindah_keluar(request, pk):
    keluar = get_object_or_404(PindahKeluar, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        hasil_surat = request.FILES.get('hasil_surat')
        keluar.status = status
        if hasil_surat:
            keluar.hasil_surat = hasil_surat
        keluar.save()
        messages.success(request, "Status berhasil diperbarui.")
        return redirect('detail_pengajuan_pindah_keluar', pk=pk)
    return render(request, 'admin/detail_keluar.html', {'keluar': keluar})



@login_required
def pengajuan_sktm(request):
    if request.method == 'POST':
        form = SKTMPengajuanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('home')
    else:
        form = SKTMPengajuanForm()
    return render(request, 'surat/sktm_form.html', {'form': form})

@staff_member_required
def daftar_sktm(request):
    daftar = SKTMPengajuan.objects.all().order_by('-tanggal_dibuat')
    return render(request, 'admin/daftar_sktm.html', {'daftar': daftar})

@staff_member_required
def detail_sktm(request, pk):
    sktm = get_object_or_404(SKTMPengajuan, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        hasil_surat = request.FILES.get('hasil_surat')
        sktm.status = status
        if hasil_surat:
            sktm.hasil_surat = hasil_surat
        sktm.save()
        messages.success(request, "Status berhasil diperbarui.")
        return redirect('detail_pengajuan_sktm', pk=pk)
    return render(request, 'admin/detail_sktm.html', {'sktm': sktm})

@staff_member_required
def daftar_domisili(request):
    daftar = DomisiliPengajuan.objects.all().order_by('-tanggal_dibuat')
    return render(request, 'admin/daftar_domisili.html', {'daftar': daftar})

@login_required
def pengajuan_domisili(request):
    if request.method == 'POST':
        form = DomisiliPengajuanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('home')
    else:
        form = DomisiliPengajuanForm()
    return render(request, 'surat/domisili_form.html', {'form': form})

@staff_member_required
def detail_domisili(request, pk):
    domisili = get_object_or_404(DomisiliPengajuan, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        hasil_surat = request.FILES.get('hasil_surat')
        domisili.status = status
        if hasil_surat:
            domisili.hasil_surat = hasil_surat
        domisili.save()
        messages.success(request, "Status berhasil diperbarui.")
        return redirect('detail_pengajuan_domisili', pk=pk)
    return render(request, 'admin/detail_domisili.html', {'domisili': domisili})





@staff_member_required
def daftar_sku(request):
    sku = SKUPengajuan.objects.all().order_by('-tanggal_dibuat')
    return render(request, 'admin/daftar_sku.html', {'sku': sku})

@login_required
def pengajuan_sku(request):
    if request.method == 'POST':
        form = SKUPengajuanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengajuan berhasil dikirim.")
            return redirect('home')
    else:
        form = SKUPengajuanForm()
    return render(request, 'surat/sku_form.html', {'form': form})

@staff_member_required
def detail_sku(request, pk):
    sku = get_object_or_404(SKUPengajuan, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        hasil_surat = request.FILES.get('hasil_surat')
        sku.status = status
        if hasil_surat:
            sku.hasil_surat = hasil_surat
        sku.save()
        messages.success(request, "Status berhasil diperbarui.")
        return redirect('detail_pengajuan_sku', pk=pk)
    return render(request, 'admin/detail_sku.html', {'sku': sku})


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


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            nik = form.cleaned_data['nik']
            email = form.cleaned_data['email']
            nama = form.cleaned_data['nama']
            alamat = form.cleaned_data['alamat']
            password = form.cleaned_data['password']

            # Buat user baru
            user = User.objects.create_user(username=nik, email=email, password=password)
            # Buat profil user dengan data nama dan alamat
            UserProfile.objects.create(user=user, nama=nama, alamat=alamat)

            messages.success(request, "Registrasi berhasil, silakan login.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'profile/register.html', {'form': form})


@user_passes_test(is_admin)
@staff_member_required
def admin_dashboard(request):
    akta_kelahiran = AktaKelahiran.objects.all()
    pindah_datang = PindahDatang.objects.all()
    pindah_keluar = PindahKeluar.objects.all()
    akta_kematian = AktaKematian.objects.all()
    sku = SKUPengajuan.objects.all()
    domisili = DomisiliPengajuan.objects.all()
    sktm = SKTMPengajuan.objects.all()

    semua_pengajuan = list(chain(
        akta_kelahiran,
        pindah_datang,
        pindah_keluar,
        akta_kematian,
        sku,
        domisili,
        sktm
    ))

    context = {
        'akta_kelahiran': akta_kelahiran,
        'pindah_datang': pindah_datang,
        'pindah_keluar': pindah_keluar,
        'akta_kematian': akta_kematian,
        'sku': sku,
        'domisili': domisili,
        'sktm': sktm,
        'semua_pengajuan': semua_pengajuan,
    }
    return render(request, 'admin/dashboard.html', context)

