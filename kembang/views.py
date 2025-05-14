# pelayanan/views.py
from django.shortcuts import render, redirect
from .forms import PengajuanSuratForm

def ajukan_surat(request):
    if request.method == 'POST':
        form = PengajuanSuratForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'kembang/sukses.html')
    else:
        form = PengajuanSuratForm()
    return render(request, 'kembang/pelayanan.html', {'form': form})
