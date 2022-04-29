from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'category',
        'image',
        'colour',
        'sale_type',
    )
    ordering = ('-sku',)

#the order can be chang is using the name or not sku!

class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product)
admin.site.register(Category)

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoriesAdmin)
