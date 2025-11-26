import csv
from celery import shared_task
from django.conf import settings
from products.models import Product
from django.db import transaction

@shared_task
def process_csv_task(file_path, task_id):
    total_rows = sum(1 for _ in open(file_path)) - 1
    processed = 0
    batch_size = int(settings.BATCH_SIZE)
    batch = []

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            batch.append(row)
            if len(batch) >= batch_size:
                save_batch(batch)
                processed += len(batch)
                batch = []
    # save remaining
    if batch:
        save_batch(batch)
        processed += len(batch)

    return {"status": "completed", "processed": processed, "total": total_rows}

def save_batch(batch):
    for item in batch:
        sku = item["sku"]
        product, created = Product.objects.update_or_create(
            sku_normalized=sku.lower(),
            defaults={
                "sku": sku,
                "name": item.get("name"),
                "description": item.get("description"),
                "price": float(item.get("price")),
                "active": True
            }
        )
