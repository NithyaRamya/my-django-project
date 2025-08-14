# app/models.py
from django.db import models

class HomeBanner(models.Model):
    title = models.CharField(max_length=200)
    house_image = models.ImageField(upload_to='house_images/')
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description1 = models.TextField(max_length=100,blank=True, null=True)
    description2 = models.TextField(max_length=100,blank=True, null=True)
    background_image = models.ImageField(upload_to='banner_images/')
    house_image = models.ImageField(upload_to='house_images/')

    def __str__(self):
        return self.title
