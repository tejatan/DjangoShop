from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models import Product  # Import Product from store app




class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product
    
@receiver(post_save, sender=CartItem)
def cart_item_post_save_receiver(sender, instance, created, **kwargs):
    cart_obj = instance.cart
    total = 0
    for item in cart_obj.cartitem_set.all():
        total += item.sub_total()
    cart_obj.save()
    cart_obj.total = total
    cart_obj.save()
