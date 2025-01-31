from django.db import models # models.py
from django.urls import reverse



class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
        

    def __str__(self): # type: ignore
        return self.product_name
    
    def __str__(self): # type: ignore
        return '{}'.format(self.product_name)
    
    def __str__(self):
        return '{}'.format(self.category)   
    
    
    