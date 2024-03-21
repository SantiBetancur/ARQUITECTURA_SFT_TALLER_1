from django.db import models

# Create your models here.
class communities(models.Model):
    name = models.CharField(max_length = 30)
    sellers = models.IntegerField(null = False)
    products = models.IntegerField(null = True)
    image = models.ImageField(upload_to="Images", null=True)
    location = models.CharField(null = False, max_length=30)

