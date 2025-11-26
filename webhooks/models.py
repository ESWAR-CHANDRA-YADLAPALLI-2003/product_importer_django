from django.db import models

class Webhook(models.Model):
    EVENT_CHOICES = (
        ("product_imported", "Product Imported"),
        ("product_updated", "Product Updated"),
    )

    url = models.URLField()
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.url
