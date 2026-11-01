from django import forms
from django.utils import timezone
from .models import Randevu

class RandevuForm(forms.ModelForm): # .save() ile doğrudan verileri db yazabilir.
    class Meta: # Formun modelle bağlantısını anlatan ayar bölümü
        model = Randevu #bu form hangi modelin formu
        fields = ['kisi_adi', 'doktor', 'telefon_no', 'tarih_saat','notlar']
        labels = {
            'kisi_adi': 'Kişi adı',
            'doktor': 'Doktor',
            'telefon_no': 'Telefon',
            'tarih_saat': 'Tarih ve saat',
            'notlar': 'Notlar'
        }

        widgets = {
            'tarih_saat': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M', #type:"datetime_local" kutusu değeri sadece bu şekilde kabul eder
            ),
            'notlar': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doktor'].empty_label = 'Doktor seçiniz'

    def clean_tarih_saat(self): #Bir alan için özel doğrulama yazmak için clean_+alan_adı olmalı. is_valid() çağrıldığıda bunu otomatik çalıştırır.
        tarih = self.cleaned_data['tarih_saat']
        if tarih < timezone.now():
            raise forms.ValidationError('Geçmiş bir tarihe randevu oluşturamazsınız!')
        return tarih