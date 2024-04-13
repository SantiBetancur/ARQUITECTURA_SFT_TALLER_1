from django.db import models

# Create your models here.


class products(models.Model):
    name = models.CharField(max_length = 40)
    price = models.CharField(max_length = 10)
    description = models.TextField(max_length = 250)
    image = models.ImageField(upload_to="images/", null=True)
    rating = models.IntegerField(null = True, default = 0)
  

