from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.username}"


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
    price_history = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    def get_current_price(self):
        """Returns the current price of the product based on price history."""
        if not self.price_history:
            return None
        return self.price_history[list(self.price_history.keys())[-1]]

    def update_price(self, price, timestamp=None):
        """Updates the product price history with a new price and timestamp."""
        if timestamp is None:
            timestamp = timezone.now()
        self.price_history.update({str(timestamp): price})
        self.save()


class ProductMedia(models.Model):
    """Model for storing product photos and videos."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField(upload_to='products/')
    media_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])

    class Meta:
        verbose_name = 'Product Media'


class Banner(models.Model):
    BANNER_TYPES = (
        ('mainBanner', 'Main_Banner'),
        ('adBanner', 'Ad_Banner'),
    )
    banner_type = models.CharField(max_length=255, choices=BANNER_TYPES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/')
    butt_link = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.banner_type}"
