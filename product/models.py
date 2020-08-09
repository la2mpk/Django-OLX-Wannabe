from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Product(models.Model):

    CONDITION_TYPE = [
        ('New', 'New'),
        ('Used', 'Used')
    ]

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.brand_name
