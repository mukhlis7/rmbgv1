from django.db import models

# Create your models here.

# models.py
class ImgToProc(models.Model):
    name = models.CharField(max_length=50,default="nothing")
    Image_To_Process = models.ImageField(upload_to='images/')