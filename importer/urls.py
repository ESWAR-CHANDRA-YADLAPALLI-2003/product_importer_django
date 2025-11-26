from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('summary/', views.upload_file, name='summary'),
    path('products/', views.product_list, name='product_list'),
    path('product/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('products/bulk_delete/', views.bulk_delete_products, name='bulk_delete_products'),
    path('webhooks/', views.webhook_list, name='webhook_list'),
    path('webhook/add/', views.webhook_edit, name='webhook_add'),
    path('webhook/edit/<int:pk>/', views.webhook_edit, name='webhook_edit'),
    path('webhook/delete/<int:pk>/', views.webhook_delete, name='webhook_delete'),
    path('webhook/test/<int:pk>/', views.webhook_test, name='webhook_test'),
]
