from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
class Category(models.Model):
    category = models.CharField(("Kategori"), max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category

class Card(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Ürün Adı"),max_length=50)
    text = models.TextField(("Ürün Özellikleri"), null=True , max_length=1000)
    price = models.IntegerField(("Ürün Fiyatı"))
    image = models.FileField(("Ürün Resmi"), upload_to='', max_length=100)
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True)
    categorys = models.ManyToManyField(Category, verbose_name=("category"))
    stars = models.FloatField(("Puan"),null=True, default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Card, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Beden(models.Model):
    title = models.CharField(("Beden"), max_length=50)
    slug = models.SlugField(("Slug Beden"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Beden, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Numara(models.Model):
    title = models.CharField(("Numara"), max_length=50)

    def __str__(self):
        return self.title
    
class EBeden(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    card = models.ForeignKey(Card, verbose_name=("Ürün"), on_delete=models.CASCADE)
    price = models.IntegerField(("Ürün Fiyatı"),default=0)
    stok = models.IntegerField(("Stok"), default=0)
    beden = models.ForeignKey(Beden, verbose_name=("Beden"), on_delete=models.CASCADE)

    def __str__(self):
        return self.card.title

class ANumara(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    card = models.ForeignKey(Card, verbose_name=("Ürün"), on_delete=models.CASCADE)
    price = models.IntegerField(("Ürün Fiyatı"),default=0)
    stok = models.IntegerField(("Stok"), default=0)
    beden = models.ForeignKey(Numara, verbose_name=("Numara"), on_delete=models.CASCADE)

    def __str__(self):
        return self.card.title
    
class Favori(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE, null=True)
    urun = models.ForeignKey(Card, verbose_name=("Ürün"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.urun.title
    
class Comment(models.Model):
    card = models.ForeignKey(Card, verbose_name=("Kart"), on_delete=models.CASCADE)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"), max_length=1000)
    user = models.ForeignKey(User, verbose_name=("Yorumcu"), on_delete=models.CASCADE, null=True)
    date_now = models.DateTimeField(("Paylaşım Zamanı"),auto_now_add=True)
    star = models.IntegerField(("Yorum Puanı"), default=0)

    def __str__(self):
        return self.card.title 
    
# USER MODEL
    
class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    password = models.CharField(("Şifre"), max_length=50)
    phone_number = models.CharField(("05---------"), max_length=50, null=True, default='Telefon Numarası')
    address = models.CharField(("Adres"), max_length=100, default='Adres')
    image = models.FileField(("Profil Fotoğrafı"), upload_to=None, max_length=100, default='None/defaultProfil.webp')
    urunadet = models.IntegerField(("Ürün Adet"),null=True, blank=True,default=0)
    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(("İsim"), max_length=50)
    email = models.EmailField(("Mail"), max_length=254)
    title = models.CharField(("Konu"), max_length=50)
    text = models.TextField(("Mesaj"), max_length=500)

    def __str__(self):
        return self.name
    
class SepetUrun(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    Eurun = models.ForeignKey(EBeden, verbose_name=("EÜrün"), on_delete=models.CASCADE,null=True)
    Aurun = models.ForeignKey(ANumara, verbose_name=("AÜrün"), on_delete=models.CASCADE,null=True)
    toplamFiyat = models.FloatField(("Toplam Fiyat"), default=0)
    adet = models.IntegerField(("Adet"),default=0)
    
    
