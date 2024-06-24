from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Product


@receiver(pre_save, sender=Product)
def ProductPreSave(sender,instance,**kwargs):
    print(f"\n befor product {instance.name} saved to database \n")


@receiver(post_save, sender=Product)
def ProductPostSave(sender,instance,**kwargs):
    print(f"\n after product {instance.name} saved to database \n")