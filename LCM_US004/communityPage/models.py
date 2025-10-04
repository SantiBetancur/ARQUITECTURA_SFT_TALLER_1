from django.db import models
from django.contrib.auth.models import User as DjangoUser
from Sellerprofile.models import Seller

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="images/communities/", null=True)
    location = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def sellers_count(self):
        return self.communityseller_set.count()
    
    @property
    def products_count(self):
        from community_main_page.models import Product
        return Product.objects.filter(community=self).count()


class CommunitySeller(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['community', 'seller']
    
    def __str__(self):
        return f"{self.seller.user.username} in {self.community.name}"

