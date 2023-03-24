from django.db import models

# Create your models here.
class Image(models.Model):
   id = models.IntegerField(primary_key=True)
   main_Img = models.ImageField(upload_to='images/')