from django.db import models


# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="parent", blank=True, null=True)
    title = models.CharField(max_length=50, verbose_name='title')
    description = models.TextField(verbose_name='description')
    avatar = models.ImageField(blank=True, null=True, upload_to='catgories/', verbose_name='avatar')
    is_enabled = models.BooleanField(default=True, verbose_name='is enabled?')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    description = models.TextField(verbose_name='description', blank=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='')
    is_enable = models.BooleanField(default=True, verbose_name='is enabled?')
    categories = models.ManyToManyField("Category", verbose_name='category', blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        db_table = 'products'
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class File(models.Model):
    product = models.ForeignKey("Product", verbose_name="product", related_name="files", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='title')
    file = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='file')
    is_enable = models.BooleanField(default=True, verbose_name='is enabled?')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        db_table = 'files'
        verbose_name = "File"
        verbose_name_plural = "Files"
