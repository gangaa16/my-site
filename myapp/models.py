from distutils.command.upload import upload
from email.mime import image
from enum import unique
from pyexpat import model
from re import T
from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to ='images')
