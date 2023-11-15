from django.db import models

# Create your models here.


class jual(models.Model):
    nama = models.CharField(max_length=200)
    keterangan = models.TextField()
    
    def __str__(self):
        return f"{self.nama}"
    
class beli(models.Model):
    nama = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nama}"