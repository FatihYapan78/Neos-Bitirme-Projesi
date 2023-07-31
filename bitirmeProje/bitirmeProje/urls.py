"""bitirmeProje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('post/<categoryid>/', kategori, name='kategori'),
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
