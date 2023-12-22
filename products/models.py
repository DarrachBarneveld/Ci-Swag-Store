from django.db import models
from decimal import Decimal


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sale = models.IntegerField(default=0, null=True, blank=True)


    @property
    def rating_array(self):
        return ['item' for _ in range(round(self.rating))]

    @property
    def total_final_price(self):
        discounted_amount = (self.sale / Decimal(100)) * self.price
        result = self.price - discounted_amount
        return result.quantize(Decimal('0.00'))

    def __str__(self):
        return self.name
