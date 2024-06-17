from datetime import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#
#     def __str__(self):
#         return f"{self.username}"


class Category(models.Model):
    """Model for product categories with tree structure (max depth 5)."""

    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.get_root().name + ' -> ' + self.name

    def get_root(self):
        """Returns the root category of the current category."""
        if self.parent is None:
            return self
        return self.parent.get_root()


class Product(models.Model):
    """Model for products with ability to track price changes over time."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    views_count = models.PositiveIntegerField(default=0)
    # price_history = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    # def get_current_price(self):
    #     """Returns the current price of the product based on price history."""
    #     if not self.price_history:
    #         return None
    #     return self.price_history[list(self.price_history.keys())[-1]]
    #
    # def update_price(self, price, timestamp=None):
    #     """Updates the product price history with a new price and timestamp."""
    #     if timestamp is None:
    #         timestamp = timezone.now()
    #     self.price_history.update({str(timestamp): price})
    #     self.save()


class ProductMedia(models.Model):
    """Model for storing product photos and videos."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='products/')
    media_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])

    class Meta:
        verbose_name = 'Product Media'


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.price} ({self.timestamp})"


class Banner(models.Model):
    BANNER_TYPES = (
        ('mainBanner', 'Main_Banner'),
        ('py manage.py runserver', 'Ad_Banner'),
    )
    banner_type = models.CharField(max_length=255, choices=BANNER_TYPES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/')
    butt_link = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.banner_type}"


class DiscountCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    applicable_products = models.ManyToManyField(Product, blank=True)
    applicable_categories = models.ManyToManyField('Category', blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', related_name='carts')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Cart for {self.user}"
