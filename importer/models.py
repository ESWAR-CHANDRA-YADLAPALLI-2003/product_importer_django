from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    sku = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)  # Not in CSV, default True

    def __str__(self):
        return self.title
class Webhook(models.Model):
    url = models.URLField(unique=True)
    event_type = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} -> {self.url}"
