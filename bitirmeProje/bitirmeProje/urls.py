from django.contrib import admin
from django.urls import path
from appBitirme.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('iletisim/', iletisim, name='iletisim'),
    path('magaza/', magaza, name='magaza'),
    path('post/<categoryslug>/', kategori, name='kategori'),
    path('cardDelete/<did>', cardDelete,name='cardDelete'),
    path('sepet/', sepet, name='sepet'),
    path('urunDelete/<id>', urunDelete, name='urunDelete'),
    # USER
    path('uyelik/', uyelik , name='uyelik'), # Üye Girişi
    path('uyekayit/', uyekayit, name='uyekayit'), # Üye Olmak
    path('logout/', Logout, name="Logout"), # Üye Çıkış
    path('sifreDegistir/', sifreDegistir, name='sifreDegistir'),
    path('profil/', profil, name='profil'),
    path('detail/<slug>/', detail, name='detail'),
    path('sifreunutma/', sendMail, name='sifreunutma'),
    # Search 
    path('search/', search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
