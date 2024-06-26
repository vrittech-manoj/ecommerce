from django.db import models

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length = 444)


    def __str__(self) -> str:
        return self.cat_name
    

class Product(models.Model):
    name = models.CharField(max_length = 444)
    categories = models.ManyToManyField(Category)
   

    def __str__(self) -> str:
        return self.name

