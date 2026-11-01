from django.db import models
from django.utils import timezone

# Create your models here.

class Doktor(models.Model):
    ad = models.CharField(max_length = 100)
    alan = models.CharField(max_length = 100)

    class Meta:
        ordering = ['ad']
        verbose_name_plural = 'Doktorlar'

    def __str__(self):
        return f"{self.ad} ({self.alan})"

class Randevu(models.Model): #models.Model'den miras alımı bu sayede hazır özellikler gelir
    class Durum(models.TextChoices):
        AKTIF ='aktif', 'Aktif' #TextChoices her satırda tam 2 parça bekler: değer, etiket. İlki veritabanında yazılan değer, ikincisi admin ve formlarda görünen etiket
        IPTAL = 'iptal', 'İptal edildi'


    kisi_adi = models.CharField(max_length = 100)
    doktor = models.ForeignKey(
        Doktor,
        on_delete=models.PROTECT, #PROTECT - Randevusu olan doktor silinemez, Django hata verir
        null = True,
        related_name='randevular',
    )
    telefon_no = models.CharField(max_length = 15, blank = True)
    #blank - formda boş bırakılabilir, IntegerField deseydik baştaki sıfır kaybolurd ve +90 yazılamaz.Üzerind etoplama vs yapılmasın diye metin olarak tutulur
    tarih_saat = models.DateTimeField()
    notlar = models.TextField(blank = True)
    #CharField'ın uzun hali, çok satırlı kutu
    durum = models.CharField(max_length = 20, choices = Durum.choices, default = Durum.AKTIF)
    olusturulma_tarihi = models.DateTimeField(auto_now_add = True)
    #randevu ilk oluşturulduğu anda Django saati kendisi yazar
    #auto_now = True olsaydı her güncellemede değişirdi.

    class Meta:
        ordering = ['tarih_saat']
        verbose_name_plural = 'Randevu'

    def __str__(self):
        yerel = timezone.localtime(self.tarih_saat)
        return f"{self.kisi_adi} - {yerel:%d.%m.%Y - %H:%M}"




