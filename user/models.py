from django.db import models
from django.contrib.auth.models import User
from user.models import *
from ckeditor.fields import RichTextField


# Create your models here.


class Hesap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    ad = models.CharField(max_length=100, null=True)    
    soyad = models.CharField(max_length=100, null=True)
    telefon = models.IntegerField(null=True)        

    def __str__(self):
        return self.user.username

class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim
    
class Post(models.Model):
    olusturan = models.OneToOneField(User, on_delete=models.CASCADE)
    kategori = models.ForeignKey(Kategori,on_delete=models.SET_NULL,null=True)
    isim = models.CharField(max_length=100)
    aciklama = RichTextField(max_length=500, null=True)
    fiyat = models.IntegerField()    
    resim = models.FileField(upload_to = 'urunler/',null=True)
    