from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(max_length=250)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='cateimages',blank=True)





    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('shop:product_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)



class Product(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    description=models.TextField(max_length=2050)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    images=models.ImageField(upload_to="proimages")
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)




    def get_url(self):
        return reverse('shop:prodCatdetail',args=[self.category.slug,self.slug])


    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)
