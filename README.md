# Randevu Takip Uygulaması
Django ile geliştirilmiş, randevu oluşturma, düzenleme, iptal etme ve yaklaşan randevuları listeleme işlemlerini yapan bir web uygulamasıdır.

## Özellikler

- Randevu oluşturma (başlık, kişi adı, telefon, tarih-saat, notlar)
- Randevu düzenleme
- Randevu iptal etme(kayıt silinmez, durumu "iptal" olur.)
- Yaklaşan randevuları tarihe göre sıralı listeleme
- Geçmiş traihe randevu oluşturmayı engelleyen form doğrulaması
- İşlem sonrası bildirim mesajları

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

Tarayıcıda `http://127.0.0.1:8000/` adresini açın.
Yönetim Paneli içinse `http://127.0.0.1:8000/admin/` adresini açın.

Mac/Linux kullanıcısı iseniz sanal ortamı `source venv/bin/activate` ile aktif ediniz.

## Proje Yapısı

```
randevu_takip/
|- config/       # Proje ayarları ve ana URL yönlendirmesi
|- randevular/   # Uygulama: model, form, view, url
|- static/css/   # CSS dosyları
|- templates/    # HTML şablonları
|- manage.py
```
