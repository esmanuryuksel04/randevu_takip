from django.urls import path
from . import views #aynı klasördeki views.py'yi içe aktarır

app_name = 'randevular' # Bu app'in URL'lerine isim alanı verir. Kullanımı -> randevular:liste

urlpatterns = [
    path('', views.randevu_listesi, name='liste'),
    path('yeni/', views.randevu_olustur, name='olustur'),
    path('<int:pk>/duzenle/', views.randevu_duzenle, name='duzenle'),
    path('<int:pk>/iptal/', views.randevu_iptal, name='iptal'),
]