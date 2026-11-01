from django.contrib import admin
from .models import Randevu, Doktor #noktanın anlamı- bu klasördeki

# Register your models here.

@admin.register(Randevu)
class RandevuAdmin(admin.ModelAdmin):
    list_display = ('kisi_adi', 'tarih_saat', 'durum')
    list_filter = ('durum', 'doktor') #sağ tarafa duruma göre filtre kutusu ekler
    search_fields = ('kisi_adi',) #üstte arama kutusu çıkarır. eğer köşeli parantezle yaparsan sona virgül gerekmez!

#admin.site.register(Randevu) #modeli admin paneline tanıttık.
admin.site.register(Doktor)
