from django.db import models

# Create your models here.


class Game(models.Model):
    nama = models.CharField(max_length=200, unique=True)
    image = models.FileField(upload_to='images/')
    
    def __str__(self):
        return f"{self.nama}"
    
class Menu(models.Model):
    game_name = models.ForeignKey(Game,on_delete=models.CASCADE,to_field="nama")
    item = models.CharField(max_length=255, default="Unknown")
    nominal = models.IntegerField()
    
    def __str__(self):
        return f"{self.item} - {self.game_name}"
    
class Joki(models.Model):
    game_name = models.ForeignKey(Game,on_delete=models.CASCADE,to_field="nama")
    item = models.CharField(max_length=255, default="unknown")
    nominal = models.IntegerField()

    def __str__(self):
        return f"{self.item} - {self.game_name}"