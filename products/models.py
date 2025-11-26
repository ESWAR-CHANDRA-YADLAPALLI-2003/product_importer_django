from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    sku_normalized = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.sku_normalized = self.sku.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sku
