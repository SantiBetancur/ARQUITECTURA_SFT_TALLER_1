from django.db import models
from django.contrib.auth.models import User as django_model_user

# Create your models here.

class Seller(models.Model):
    user_info = models.ForeignKey(django_model_user, on_delete = models.CASCADE, default = 1)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    description = models.TextField(max_length=400)
    photo = models.ImageField(upload_to='seller_photos/', null=True, blank=True)
    permission = models.FileField(upload_to='documents/', null=True)
