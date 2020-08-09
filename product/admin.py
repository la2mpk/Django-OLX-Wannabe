from django.contrib import admin
from . import models


class ProductImagesInline(admin.TabularInline):
    model = models.ProductImages
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = ProductImagesInline

    list_filter = ['created']
    search_fields = ['category', 'brand']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)
admin.site.register(models.Brand)
