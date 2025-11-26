import csv
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Webhook
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .forms import UploadFileForm, WebhookForm
import requests
# def upload_file(request):
#     return render(request, "importer/upload.html")


def upload_file(request):
    file = forms.FileField(label='Select a CSV file')
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["file"]

            # Decode file
            decoded = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded)

            imported = []
            errors = []

            for row in reader:
                try:
                    product = Product.objects.create(
                        title=row.get("title", ""),
                        description=row.get("description", ""),
                        price=row.get("price", 0),
                        stock=row.get("stock", 0),
                        sku=row.get("sku", ""),
                    )
                    imported.append(product)
                except Exception as e:
                    errors.append({"row": row, "error": str(e)})

            return render(request, "importer/summary.html", {
                "imported": imported,
                "errors": errors
            })
    else:
        form = UploadFileForm()

    return render(request, "importer/upload.html", {"form": form})

def summary(request):
    return render(request, "importer/summary.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "importer/products.html", {"products": products})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        product.title = request.POST.get("title", product.title)
        product.description = request.POST.get("description", product.description)
        product.price = float(request.POST.get("price", product.price))
        product.stock = int(request.POST.get("stock", product.stock))
        product.active = request.POST.get("active") == "on"
        product.save()
        messages.success(request, f"Product {product.sku} updated successfully.")
        return redirect('product_list')

    return render(request, "importer/edit_product.html", {"product": product})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, f"Product {product.sku} deleted successfully.")
        return redirect('product_list')
    return render(request, "importer/delete_product.html", {"product": product})


def bulk_delete_products(request):
    if request.method == "POST":
        Product.objects.all().delete()
        messages.success(request, "All products have been deleted successfully.")
        return redirect('product_list')
    return render(request, "importer/bulk_delete.html")


# List webhooks
def webhook_list(request):
    webhooks = Webhook.objects.all()
    return render(request, "importer/webhooks.html", {"webhooks": webhooks})

# Add/Edit webhook
def webhook_edit(request, pk=None):
    if pk:
        webhook = Webhook.objects.get(pk=pk)
    else:
        webhook = None

    if request.method == "POST":
        form = WebhookForm(request.POST, instance=webhook)
        if form.is_valid():
            form.save()
            return redirect('webhook_list')
    else:
        form = WebhookForm(instance=webhook)

    return render(request, "importer/webhook_form.html", {"form": form, "webhook": webhook})

# Delete webhook
def webhook_delete(request, pk):
    webhook = Webhook.objects.get(pk=pk)
    if request.method == "POST":
        webhook.delete()
        return redirect('webhook_list')
    return render(request, "importer/webhook_delete.html", {"webhook": webhook})

# Test webhook
def webhook_test(request, pk):
    webhook = Webhook.objects.get(pk=pk)
    try:
        response = requests.post(webhook.url, json={"test": "data"})
        result = f"Status Code: {response.status_code}"
    except Exception as e:
        result = str(e)
    return render(request, "importer/webhook_test.html", {"webhook": webhook, "result": result})
