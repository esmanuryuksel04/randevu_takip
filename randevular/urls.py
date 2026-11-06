from django.urls import path
from . import views #aynı klasördeki views.py'yi içe aktarır

app_name = 'randevular' # Bu app'in URL'lerine isim alanı verir. Kullanımı -> randevular:liste

urlpatterns = [
    path('', views.randevu_listesi, name='liste'),
    path('yeni/', views.randevu_olustur, name='olustur'),
    path('gecmis/', views.gecmis_randevular, name ='gecmis'),
    path('iptal-edilenler/', views.iptal_edilenler, name='iptal_edilenler'),
    path('<int:pk>/duzenle/', views.randevu_duzenle, name='duzenle'),
    path('<int:pk>/iptal/', views.randevu_iptal, name='iptal'),
    path('<int:pk>/geri-al/', views.randevu_geri_al, name='geri_al'),
]