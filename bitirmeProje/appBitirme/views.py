from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def urunAdet(request):
    if request.user.is_authenticated:
        return SepetUrun.objects.filter(user=request.user)
    else:
        return None

def index(request):
    card = Card.objects.all()[:3]
    categorys = Category.objects.all()
    context={
        'card':card,
        'categorys':categorys,
        'urunAdet':urunAdet(request),
    }
    return render(request, 'index.html', context)

def sendMail(request):
    context={
        'urunAdet':urunAdet(request),
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        userinfo = UserInfo.objects.get(user=user)
        subject = 'PAROLA HATIRLATMA'
        message = 'PAROLANIZ: ' + userinfo.password
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail( subject, message, email_from, recipient_list )
        messages.success(request,'Şifreniz E-Posta adresinize gönderilmiştir.')
        return redirect('uyelik')
    else:
        return render(request, 'user/sifreunutma.html', context)
    
# @login_required()
def iletisim(request):
    context={
        'urunAdet':urunAdet(request),
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        konu = request.POST['konu']
        mesaj = request.POST['mesaj']
        contact = Contact(name=name, email=email, title=konu, text=mesaj)
        contact.save()
        return redirect('iletisim')
    return render(request, 'iletisim.html', context)

def isAdmin(user):
    return user.is_superuser

# @user_passes_test(isAdmin)
def magaza(request):
    card = Card.objects.all()
    categorys = Category.objects.all()
    if request.method == 'POST':
        if request.POST.get('submit') == 'urunDuzen':
            cardid = request.POST.get('cardid')
            urun = card.get(id=cardid)
            title = request.POST.get('title')
            price = request.POST.get('price')
            image = request.FILES.get("image")
            if image is None:
                image = urun.image
            urun.title = title
            urun.price = price
            urun.image = image
            urun.save()
            return redirect('magaza')
        if request.POST.get('submit') == 'sepetButon':
            urid = request.POST.get('urid')
            urun = card.get(id=urid)
            adet = 1
            beden = "S"  
            numara = 40
            urun = Card.objects.filter( id = urid )
            urun = urun.get()
            urunE = EBeden.objects.filter(card__title=urun,beden__title=beden)
            if urunE.exists():
                urunE = urunE.get()
                toplamFiyat = urunE.price * adet
                urunid = SepetUrun.objects.filter(user = request.user, Eurun=urunE)
                if urunid.exists():
                    urunid = urunid.get()
                    urunid.adet += adet
                    urunid.toplamFiyat += toplamFiyat
                    urunid.save()
                else:
                    sepetu = SepetUrun(user = request.user, Eurun=urunE, toplamFiyat=toplamFiyat,adet=adet)
                    sepetu.save()
            urunA = ANumara.objects.filter(card__title=urun,beden__title=numara)
            if urunA.exists():
                urunA = urunA.get()
                toplamFiyat = urunA.price * adet
                uruna = SepetUrun.objects.filter(user = request.user, Aurun=urunA)
                if uruna.exists():
                    uruna = uruna.get()
                    uruna.adet += adet
                    uruna.toplamFiyat += toplamFiyat
                    uruna.save()
                else:
                    sepetu = SepetUrun(user = request.user, Aurun=urunA, toplamFiyat=toplamFiyat,adet=adet)
                    sepetu.save()
            return redirect('magaza')
    paginator = Paginator(card, 6)
    page_number = request.GET.get('page')
    card = paginator.get_page(page_number)
    context={
        'card':card,
        'categorys':categorys,
        'urunAdet':urunAdet(request),
    }
    return render(request, 'magaza.html', context)

def kategori(request,categoryid):
    card = Card.objects.filter(categorys=categoryid)
    categorys = Category.objects.all()
    if request.method == 'POST':
        if request.POST.get('submit') == 'urunDuzen':
            cardid = request.POST.get('cardid')
            urun = card.get(id=cardid)
            title = request.POST.get('title')
            price = request.POST.get('price')
            image = request.FILES.get("image")
            if image is None:
                image = urun.image
            urun.title = title
            urun.price = price
            urun.image = image
            urun.save()
            return redirect('magaza')
        if request.POST.get('submit') == 'sepetButon':
            urid = request.POST.get('urid')
            urun = card.get(id=urid)
            adet = 1
            beden = "S"  
            numara = 40
            urun = Card.objects.filter( id = urid )
            urun = urun.get()
            urunE = EBeden.objects.filter(card__title=urun,beden__title=beden)
            if urunE.exists():
                urunE = urunE.get()
                toplamFiyat = urunE.price * adet
                urunid = SepetUrun.objects.filter(user = request.user, Eurun=urunE)
                if urunid.exists():
                    urunid = urunid.get()
                    urunid.adet += adet
                    urunid.toplamFiyat += toplamFiyat
                    urunid.save()
                else:
                    sepetu = SepetUrun(user = request.user, Eurun=urunE, toplamFiyat=toplamFiyat,adet=adet)
                    sepetu.save()
            urunA = ANumara.objects.filter(card__title=urun,beden__title=numara)
            if urunA.exists():
                urunA = urunA.get()
                toplamFiyat = urunA.price * adet
                uruna = SepetUrun.objects.filter(user = request.user, Aurun=urunA)
                if uruna.exists():
                    uruna = uruna.get()
                    uruna.adet += adet
                    uruna.toplamFiyat += toplamFiyat
                    uruna.save()
                else:
                    sepetu = SepetUrun(user = request.user, Aurun=urunA, toplamFiyat=toplamFiyat,adet=adet)
                    sepetu.save()
            return redirect('magaza')
    paginator = Paginator(card, 6)
    page_number = request.GET.get('page')
    card = paginator.get_page(page_number)
    context={
        'card':card,
        'categorys':categorys,
        'urunAdet':urunAdet(request),
    }
    return render(request, 'category.html',context)

def sepet(request):
    urun = SepetUrun.objects.filter(user=request.user)
    uruntoplam = 0
    kargo= 15
    for i in urun:
        uruntoplam += i.toplamFiyat
    if len(urun) == 0:
        kargo = 0
    toplam = kargo + uruntoplam
    if request.method == 'POST':
        print(request.POST)
        for k,v in dict(request.POST).items():
            if k != 'csrfmiddlewaretoken':
                try:
                    v[0] = int(v[0])
                except:
                    return redirect('sepet')
                urunb = urun.get(id=k[4:])
                if urunb.Eurun:
                    urunb.adet = v[0]
                    urunb.toplamFiyat = urunb.Eurun.price * v[0]
                    urunb.save()
                if urunb.Aurun:
                    urunb.adet = v[0]
                    urunb.toplamFiyat = urunb.Aurun.price * v[0]
                    urunb.save()
        return redirect('sepet')
    context={
        'urun':urun,
        'uruntoplam':uruntoplam,
        'toplam':toplam,
        'urunAdet':urunAdet(request),
    }
    return render(request, 'sepet.html',context)

def urunDelete(request,id):
    urun = SepetUrun.objects.get(id=id)
    urun.delete()
    return redirect('sepet')

def detail(request,slug):
    card = get_object_or_404(Card, slug = slug)
    comments = Comment.objects.filter(card=card).order_by('-star')
    userinfo = UserInfo.objects.get(user=request.user)
    puan= 0
    if request.method == 'POST':
        submit = request.POST.get('submit')
        if submit == 'sepetbuton':
            beden = request.POST.get('size')
            
            try:
                adet = int(request.POST.get('adet'))   
            except:
                return redirect('/detail/'+slug+'/')
            urunE = EBeden.objects.filter(card__slug=slug,beden__title=beden)
            if urunE.exists():
                urunE = urunE.get()
                toplamFiyat = urunE.price * adet
                urunid = SepetUrun.objects.filter(user = request.user, Eurun=urunE)
                if urunid.exists():
                    urunid = urunid.get()
                    urunid.adet += adet
                    urunid.toplamFiyat += toplamFiyat
                    urunid.save()
                else:
                    sepetu = SepetUrun(user = request.user, Eurun=urunE, toplamFiyat=toplamFiyat,adet=adet)
                    sepetu.save()
            numara = request.POST.get('numara')
            urunA = ANumara.objects.filter(card__slug=slug,beden__title=numara)
            if urunA.exists():
                urunA = urunA.get()
                print(urunA)
                toplamFiyat = urunA.price * adet
                uruna = SepetUrun.objects.filter(user = request.user, Aurun=urunA)
                
                if uruna.exists():
                    uruna = uruna.get()
                    uruna.adet += adet
                    uruna.toplamFiyat += toplamFiyat
                    uruna.save()
                else:
                    sepetu = SepetUrun(user = request.user, Aurun=urunA, toplamFiyat=toplamFiyat,adet=adet)
                    sepetu.save()
            return redirect('/detail/'+slug+'/')
        elif submit == 'butonYorum':
            print(request.POST)
            title = request.POST.get('title')
            text = request.POST.get('text')
            star = request.POST.get('rating')
            yorum = Comment(card=card,user=request.user, title=title, text=text,star=star)
            yorum.save()
            for i in comments:
                puan += i.star
            card.stars = round(puan / len(comments),1)
            card.save()
            return redirect('/detail/'+slug+'/')
    listprice = []
    listbeden = []
    listnumara = []
    ebeden = EBeden.objects.filter(card=card)
    anumara = ANumara.objects.filter(card=card)
    for i in range(len(ebeden)):
        listprice.append(ebeden[i].price)
        listbeden.append(ebeden[i].beden.slug)
    for i in range(len(anumara)):
        listprice.append(anumara[i].price)
        listnumara.append(anumara[i].beden.title)
    context = {
        "card" : card,
        'urunAdet':urunAdet(request),
        'comments':comments,
        'userinfo':userinfo,
        'listprice':listprice,
        'listbeden':listbeden,
        'listnumara':listnumara,
    }
    return render(request, 'detail.html', context)

# USER
def uyelik(request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        harfet = False
        for harf in username:
            if harf == "@":
                harfet = True
        if username[-4:] == ".com" and harfet:
            try:
                user = User.objects.get(email=username)
                username = user.username
            except:
                messages.error(request,'E-mail veya Şifre yanlış')
                return redirect('uyelik')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Kullanıcı Adı veya Şifre yanlış')
    return render(request, 'user/uyelik.html', context)

def uyekayit(request):
    context={}
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        harfup = False
        harflen = False
        harfnum = False
        for harf in password:
            if harf.isupper():
                harfup=True
                if len(harf) >= 5:
                    harflen=True
                    if harf.isnumeric():
                        harfnum = True
        if password == password2:
            if harfup and harfnum and harflen:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        user = User.objects.create_user(username=username,first_name=name, last_name=surname, email=email, password=password)
                        user.save()
                        messages.success(request, 'Üyeliğiniz başarılı bir şekilde oluşturulmuştur.')
                        userinfo = UserInfo(user=user, password=password)
                        userinfo.save()
                        return redirect('uyelik')
                    else:
                        messages.error(request,'Bu E-mail kullanılıyor!!')
                else:
                    messages.error(request,'Bu Kullanıcı Adı kullanılıyor!!') 
            else:
                messages.error(request,'Şifre en az bir büyük harf içermelidir.')
                messages.error(request,'Şifre en az bir sayı içermelidir.')
                messages.error(request,'Şifre en az 5 karakter uzunluğunda olmalıdır.')
        else:
            messages.error(request,'Şifreler aynı değil!! Tekrar deneyin')
    return render(request, 'user/uyekayit.html',context)

def Logout(request):
    logout(request)
    return redirect('index')

def sifreDegistir(request):
    userinfo = UserInfo.objects.get(user=request.user)
    print(userinfo.password)
    context={
        'urunAdet':urunAdet(request),
    }
    if request.method == 'POST':
        password = request.POST['password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.get(username=request.user) # Girişli kullanıcıyı seçer.
        if user.check_password(password): # Eski parolayı kontrol et
            if password1 != " ":
                if password1 == password2:
                    user.set_password(password1)
                    user.save()
                    userinfo.password = password1
                    userinfo.save()
                    logout(request)
                    return redirect('uyelik')
                else:
                    messages.error(request,'Şifreler uyumsuz!!')
            else:
                messages.error(request,'Yeni Şifre kısmı boş bırakılamaz')
        else:
            messages.error(request,'Eski şifreniz yanlış!!')
    return render(request, 'user/sifreDegistir.html', context)

def profil(request):
    context={
        'urunAdet':urunAdet(request),
    }
    user = User.objects.get(username=request.user)
    userinfo = UserInfo.objects.get(user=user)
    # Profil Edit
    if request.method == 'POST':
        if request.POST['formbuton'] == 'profilChange': #buton kontrol
            password = request.POST['password']
            if user.check_password(password):
                username = request.POST['username']
                image = request.FILES.get('image')
                user.username = username
                user.save()
                userinfo.image = image
                userinfo.save()
                messages.success(request,'Profiliniz başarılı bir şekilde düzenlenmiştir.')
                return redirect('profil')
            
    # Full Name Change
    if request.method == 'POST':
        if request.POST['formbuton'] == 'fullNameChange': #buton kontrol
            password = request.POST['password']
            if user.check_password(password):
                name = request.POST['name']
                surname = request.POST['surname']
                user.first_name = name
                user.last_name = surname
                messages.success(request,'Adınız ve Soyadınız başarılı bir şekilde değiştirilmiştir.')
                user.save()
                return redirect('profil')
            
    # E-mail Change
    if request.method == 'POST':
        if request.POST['formbuton'] == 'emailChange': #buton kontrol
            password = request.POST['password']
            if user.check_password(password):
                email = request.POST['email']
                user.email = email
                messages.success(request,'E-Posta Adresiniz başarılı bir şekilde değiştirilmiştir.')
                user.save()
                return redirect('profil')
            
    # Phone Change
    if request.method == 'POST':
        if request.POST['formbuton'] == 'numberChange': #buton kontrol
            password = request.POST['password']
            if user.check_password(password):
                phone_number = request.POST['number']
                userinfo.phone_number = phone_number
                messages.success(request,'Telefon Numaranız başarılı bir şekilde değiştirilmiştir.')
                userinfo.save()
                return redirect('profil')
            
    # Adres Change
    if request.method == 'POST':
        if request.POST['formbuton'] == 'adresChange': #buton kontrol
            password = request.POST['password']
            if user.check_password(password):
                adres = request.POST['adres']
                userinfo.address = adres
                messages.success(request,'Adresiniz başarılı bir şekilde değiştirilmiştir.')
                userinfo.save()
                return redirect('profil')
    context.update({
        'user':user,
        'userinfo':userinfo,
        })
    return render(request, 'user/profil.html',context)

def search(request):
    if 'q' in request.GET and request.GET['q'] != "":
        q = request.GET['q']
        card = Card.objects.filter(title__contains=q)
        category = Category.objects.all()
    else:
        return redirect('magaza')
    return render(request, 'magaza.html',{
        "category":category,
        "card":card,
    })

def cardDelete(request,did):
    card = Card.objects.get(id=did)
    card.delete()
    return redirect('magaza')

