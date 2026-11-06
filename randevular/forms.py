from datetime import datetime
from django import forms
from django.utils import timezone
from .models import Randevu

def saat_dilimleri():
    dilimler = []
    for baslangic, bitis in [(9*60, 12*60), (13*60, 17*60)]: #09:00 - 12:00 ve 13:00 - 17:00
        for dakika in range(baslangic, bitis, 20):
            saat = f'{dakika // 60:02d}:{dakika % 60:02d}' #02d -> bulunan sayısal değer her zaman iki haneli olur ve hane dolmazsa başına 0 konur
            dilimler.append((saat,saat))
    return dilimler

class RandevuForm(forms.ModelForm):
    tarih = forms.DateField(
        label = 'Tarih',
        widget = forms.DateInput(attrs={'type':'date'}, format= '%Y-%m-%d'),
    )
    saat = forms.ChoiceField(
        label = 'Saat',
        choices = [('', 'Saat seçiniz')] + saat_dilimleri()
    )
    field_order = ['kisi_adi', 'doktor', 'telefon_no', 'tarih', 'saat', 'notlar']

    class Meta:
        model = Randevu
        fields = ['kisi_adi', 'doktor', 'telefon_no', 'notlar']
        labels = {
            'kisi_adi' : 'Kişi adı',
            'doktor' : 'Doktor',
            'telefon_no' : 'Telefon',
            'notlar' : 'Notlar',
        }
        widgets = {
            'notlar' : forms.Textarea(attrs={'rows' : 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doktor'].empty_label = 'Doktor seçiniz'
        if self.instance.pk:
            yerel = timezone.localtime(self.instance.tarih_saat)
            self.initial['tarih'] = yerel.date()
            self.initial['saat'] = yerel.strftime('%H:%M')

    def clean(self):
        cleaned_data = super().clean()
        tarih = cleaned_data.get('tarih')
        saat = cleaned_data.get('saat')
        doktor = cleaned_data.get('doktor')

        if not (tarih and saat):
            return cleaned_data

        saat = datetime.strptime(saat, '%H:%M').time() # "13.40" yazısını saat nesnesine çevirme
        tarih_saat = timezone.make_aware(datetime.combine(tarih, saat))
        self.instance.tarih_saat = tarih_saat

        if tarih.weekday() >= 5:
            self.add_error('tarih', 'Hafta sonu randevu alınamaz!')
        elif tarih_saat < timezone.now():
            self.add_error('tarih', 'Geçmiş bir tarihe randevu alamazsınız.')
        elif doktor and Randevu.objects.filter(
            doktor = doktor,
            tarih_saat = tarih_saat,
            durum = Randevu.Durum.AKTIF
        ).exclude(pk = self.instance.pk).exists():
            self.add_error('saat', f'{doktor.ad} bu saatte dolu, başka bir saat seçiniz.')
        return cleaned_data

