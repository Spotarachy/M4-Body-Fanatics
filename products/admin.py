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

#the order can be change by using the 'name' and not 'sku'!

class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoriesAdmin)
