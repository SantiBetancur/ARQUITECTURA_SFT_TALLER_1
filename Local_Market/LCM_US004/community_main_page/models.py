from django.db import models
from Sellerprofile.models import Seller

# Create your models here.


class products(models.Model):
    name = models.CharField(max_length = 40)
    price = models.CharField(max_length = 15)
    description = models.TextField(max_length = 250)
    image = models.ImageField(upload_to="images/", null=True)
    rating = models.IntegerField(null = True, default = 0)
    seller_info = models.ForeignKey(Seller, on_delete=models.CASCADE, default=1)
  

