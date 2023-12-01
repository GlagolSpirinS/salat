from django.db import models


# пизда шлюха член
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', null=True)
    tags = models.ManyToManyField('Tag', related_name='products')


class Order(models.Model):
    items = models.ManyToManyField('Product', through='OrderItem', related_name='orders')
    id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    fio = models.CharField(max_length=255)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)


# категория шлюх
class Category(models.Model):
    name = models.CharField(max_length=255)


# теги пидорасов
class Tag(models.Model):
    name = models.CharField(max_length=255)
