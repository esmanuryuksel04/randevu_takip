from django.contrib import admin
from .models import Randevu #noktanın anlamı- bu klasördeki

# Register your models here.

@admin.register(Randevu)
class RandevuAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'kisi_adi', 'tarih_saat', 'durum')
    list_filter = ('durum',) #sağ tarafa duruma göre filtre kutusu ekler
    search_fields = ('baslik', 'kisi_adi') #üstte arama kutusu çıkarır

#admin.site.register(Randevu) #modeli admin paneline tanıttık.
