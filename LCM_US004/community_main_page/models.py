from django.db import models
from django.contrib.auth.models import User as django_model_user
from django.db.models import Avg
from Sellerprofile.models import Seller
from communityPage.models import Community

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Better than CharField for prices
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to="images/products/", null=True)
    seller_info = models.ForeignKey(Seller, on_delete=models.CASCADE, default=1)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def average_rating(self):
        """Calculate average rating from ProductRating model"""
        ratings = ProductRating.objects.filter(product=self).aggregate(avg_rating=Avg('rating'))
        return round(ratings['avg_rating'] or 0, 2)
  
class ProductUser(models.Model):
    user_info = models.ForeignKey(django_model_user, on_delete=models.SET_NULL, null=True, default=1)
    product_info = models.ForeignKey(Product, on_delete=models.SET_NULL, default=1, null=True)
    
    def __str__(self):
        return f"{self.user_info.username} - {self.product_info.name}"


class ProductRating(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(django_model_user, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['product', 'user']  # One rating per user per product
    
    def __str__(self):
        return f"{self.user.username} rated {self.product.name} with {self.rating} stars"
    
