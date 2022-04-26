from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=600)
    friendly_name = models.CharField(max_length=600, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_deferred_fields(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=600, null=True, blank=True)
    name = models.CharField(max_length=600)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    colour = models.ImageField(null=True, blank=True)
    is_sold = models.TextField(null=True, blank=True)
    sale_type = models.TextField(null=True, blank=True)
    friendly_name = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    

    def __str__(self):
        return self.name