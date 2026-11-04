# Randevu Takip Uygulaması
Django ile geliştirilmiş, doktor randevularını oluşturma, düzenleme, iptal etme ve yaklaşan randevuları listeleme işlemlerini yapan basit bir web uygulaması.

## Özellikler

- Randevu oluşturma (kişi adı, doktor, telefon, tarih-saat, notlar)
- Randevu düzenleme
- Randevu iptal etme(kayıt silinmez, durumu "iptal" olur.)
- Yaklaşan randevuları tarihe göre sıralı listeleme
- Doktor ve muayene alanı: Doktorlar ayrı bir tabloda tutulur, her randevu bir doktora bağlıdır
- Geçmiş traihe randevu oluşturmayı engelleyen form doğrulaması
- İşlem sonrası bildirim mesajları 
- 20 dakikalık randevu dilimleri (09:00-12:00 ve 13:00-17:00, öğle arası hariç)
- Aynı doktor için aynı tarih ve saatte çakışan randevuyu engelleyen doğrulama

## Kullanılan Teknolojiler

- Python 3.11
- Django 5.2
- SQLite
- HTML, CSS, Django Template
- Git / Github

## Kurulum

``` bash
git clone https://github.com/esmanuryuksel04/randevu_takip
cd randevu_takip
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
```
Mac/Linux kullanıcısı iseniz sanal ortamı `source venv/bin/activate` ile aktif ediniz.

## İlk Kullanımı
1. `http://127.0.0.1:8000/admin/` adresine git ve oluşturduğun yönetici hesabıyla giriş yap
2. **Doktorlar** bölümünden doktor ekle (ad ve alan, örneğin "Dr. Bade Yüksel" / "Göz Hastalıkları")
3. `http://127.0.0.1:8000/` adresine dön ve **Yeni Randevu** ile randevu oluştur

## Proje Yapısı

```
randevu_takip/
|- config/       # Proje ayarları ve ana URL yönlendirmesi
|- randevular/   # Uygulama: model, form, view, url
|- static/css/   # CSS dosyları
|- templates/    # HTML şablonları
|- manage.py
```

## Veri Modeli

- **Doktor:** ad, alan
- **Randevu:** kişi adı, doktor (Doktor'a bağlı), telefon, tarih-saat, notlar, durum (aktif / iptal edildi), oluşturulma tarihi

Bir doktorun birden çok randevusu olabilir. Randevusu olan bir doktor silinemez, geçmiş kayıtlar korunur.
