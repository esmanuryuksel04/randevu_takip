# Create your views here.

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
#render: şablonu verilerle birleştirip HTML cevabı üretir, redirect: kullanıcıyı başka bir adrese yönlendirir
from django.utils import timezone

from .forms import RandevuForm
from .models import Randevu

def randevu_listesi(request):
    randevular = Randevu.objects.filter(
        durum = Randevu.Durum.AKTIF,
        tarih_saat__gte = timezone.now(), #gte -> greater than equal, tarihi şu andan sonra olanlar
        #diğer operatörler: __lt, __gt, __lte, __contains, __icontains
    ).order_by('tarih_saat')
    return render(request, 'randevular/randevu_listesi.html', {
        'randevular' : randevular,
    })

def randevu_olustur(request):
    if request.method == 'POST':
        form = RandevuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Randevu başarıyla oluşturuldu.')
            return redirect('randevular:liste')

    else:
        form = RandevuForm()
    return render(request, 'randevular/randevu_form.html', {
        'form' : form,
        'sayfa_basligi' : 'Yeni Randevu Oluştur',
    })

def randevu_duzenle(request, pk): #pk, her randevunun unique numarası
    randevu = get_object_or_404(Randevu, pk=pk)
    if request.method == 'POST':
        form = RandevuForm(request.POST, instance=randevu) #instance= : yeni kayıt değil, bu var olan kaydı düzenle
        if form.is_valid():
            form.save()
            messages.success(request, 'Randevu başarıyla güncellendi.')
            return redirect('randevular:liste')

    else:
        form = RandevuForm(instance=randevu) #GET
    return render(request,'randevular/randevu_form.html', {
        'form' : form,
        'sayfa_basligi' : 'Randevuyu Düzenle'
        })

def randevu_iptal(request, pk):
    randevu = get_object_or_404(Randevu, pk=pk)
    if request.method == 'POST':
        randevu.durum = Randevu.Durum.IPTAL
        randevu.save()
        messages.success(request, 'Randevu iptal edildi.')
        return redirect('randevular:liste')
    return render(request, 'randevular/randevu_iptal.html', {
        'randevu' : randevu,
    })


