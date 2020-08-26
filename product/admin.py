from django.contrib import admin
from .models import Product, Brand, Category, ProductImages


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 3


class ProductAdmin(admin.ModelAdmin):

    inlines = (ProductImagesInline,)

    fieldsets = [
        (None, {'fields': [y.name for y in Product._meta.fields if y.name not in ('id', 'image', 'created')]}),
        ('Main Image', {'fields': ['image']})
    ]

    list_filter = ['created']
    search_fields = ['category', 'brand', 'name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
