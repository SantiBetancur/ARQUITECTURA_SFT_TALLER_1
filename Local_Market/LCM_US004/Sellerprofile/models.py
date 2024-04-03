from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    description = models.TextField(max_length=400)
    photo = models.ImageField(upload_to='seller_photos/', null=True, blank=True)
