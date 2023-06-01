from django.db import models
from shop.models import Product

class cart(models.Model):

    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='cart'
        ordering=['date_added']
        def __str__(self):
            return  self.cart_id
class cartitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cart,models.CASCADE)
    quanity=models.IntegerField
    active=models.BooleanField(default=True)

    class Meta:
        db_table='cartitem'


    def sub_total(self):
        return self.product.price * self.quanity

    def __str__(self):
        return self.product