from django.db import models

# Create your models here.
class communities(models.Model):
    name = models.CharField(max_length = 30, null = False)
    sellers = models.IntegerField(null = True)
    products = models.IntegerField(null = True)
    image = models.ImageField(upload_to="images/", null=True)
    location = models.CharField(null = False, max_length=30)

