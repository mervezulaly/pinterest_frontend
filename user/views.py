from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User 
from .models import *
# Create your views here.


def index(request):
    return render (request,'index.html')


def userRegister(request):  
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        ad = request.POST['ad']        
        soyad = request.POST['soyad']
        telefon = request.POST['telefon']        
        sifre = request.POST['sifre']
        sifre2 = request.POST['sifre2']

        if sifre == sifre2:
            if User.objects.filter(username = kullanici).exists():
                messages.error(request,'Kullanıcı Adı Mevcut')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'Email daha önce kullanılmış')
            elif len(sifre)<6:
                messages.error(request,'Şifre 6 karakterden uzun olmalıdır')
            elif kullanici.lower() in sifre.lower():
                messages.error(request,'Kullanıcı adı ile şifre benzer olamaz')
            else:
                user = User.objects.create_user(
                    username = kullanici,
                    email = email,
                    password=sifre
                )
                Hesap.objects.create(
                    user = user, 
                    ad = ad,
                    soyad = soyad,                   
                    telefon = telefon                    
                )
                user.save()
                messages.success(request,'Kayıt Başarılı , Giriş Yapabilirsiniz')
                return redirect('login')
        else:
            messages.error(request,'Şifreler Uyuşmuyor')
    return render(request,'register.html')

def userLogin(request):    
    if request.method=="POST":
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici , password=sifre)

        if user is not None:
            login(request,user)
            messages.success(request,'Başarıyla Giriş Yapıldı')
            return redirect('index')
             
        else:
            messages.error(request,'Kullanıcı Adı veya Şifre Hatalı')
            return redirect('login')
    return render(request,'login.html')

def userLogout(request):        
    logout(request)
    messages.success(request,'Başarıyla Çıkış Yapıldı')    
    return redirect('index')

def hesap(request):
    return render(request,'hesap.html')


def pinAdd(request):
    return render(request,'pinAdd.html')