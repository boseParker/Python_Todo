from django.db import models

# Create your models here.

class Datas(models.Model):
    
    Task=models.CharField(max_length=100,default='')
    Description=models.CharField(max_length=200,default='')