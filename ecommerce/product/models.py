from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length  = 1000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/image',null = True)
    description = models.TextField()
    discount = models.IntegerField(default = 2)