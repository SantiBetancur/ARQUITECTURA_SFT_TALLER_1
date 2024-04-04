from django.db import models
from communityPage.models import communities

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 20, null = False)
    email = models.CharField(max_length = 50, null = True)
    password = models.CharField(max_length = 10, null = False)

class Seller(models.Model):
        user_info = models.ForeignKey(User, on_delete = models.CASCADE)
        seller_community = models.ForeignKey(communities, on_delete = models.CASCADE, default=1)
        seller_name = models.CharField(max_length = 50, null = False)
        age = models.IntegerField(null=False)
        permission = models.FileField(upload_to = "documents/", null=True)
        social_media = models.TextField(max_length = 200, null = True)
        phone = models.CharField(max_length = 10, null = True)
    