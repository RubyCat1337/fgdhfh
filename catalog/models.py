from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    features = models.TextField()
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category' )  
    hit = models.BooleanField(default=False)
    
    
    def get_absolute_url(self):
        return reverse("product",kwargs={"product_pk":self.pk})
    
class Comment(models.Model):
    name = models.CharField(max_length=255)
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='comments' )