from django.contrib import admin

# Register your models here.
from .models import Product,Test

admin.site.register(Test)

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','active','category']
    list_display_links=['name','price']
    list_editable=['category','active']
    search_fields=['name']
    list_filter=['category','price']
    fields=['name','category','price']


admin.site.register(Product,AdminProduct)