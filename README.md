# **Product Importer Django Application**

## **Overview**

The **Product Importer** is a Django-based web application that allows users to upload product data via CSV files and store it in a database. The application also supports webhook management for real-time event notifications. This project demonstrates skills in Django, database modeling, form handling, file processing, and REST API integration.

---

## **Features**

* Upload CSV files to bulk import product data.
* Automatic validation and error handling during CSV import.
* View imported product data in a structured table format.
* Manage webhooks to receive notifications for specific events.
* Modular Django structure with separate apps for products and webhooks.

---

## **Tech Stack**

* **Backend:** Django 5.x
* **Frontend:** Django Templates (HTML, CSS)
* **Database:** SQLite (default Django database)
* **Python Version:** 3.12
* **Other Tools:** Git for version control, Requests library for webhooks

---

## **Project Structure**

```
product_importer_django/
│
├── importer/           # Main app for CSV import and product listing
│   ├── templates/      # HTML templates
│   ├── views.py
│   ├── forms.py
│   ├── models.py
│   └── urls.py
│
├── products/           # App for product management
├── webhooks/           # App for webhook management
├── manage.py
└── requirements.txt
```

---

## **Installation & Setup**

1. **Clone the repository**:

```bash
git clone https://github.com/YourUsername/product_importer_django.git
cd product_importer_django
```

2. **Create and activate a virtual environment**:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run migrations**:

```bash
python manage.py migrate
```

5. **Start the development server**:

```bash
python manage.py runserver
```

6. **Access the application**:

Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## **Usage**

* Upload CSV files containing product information (title, description, price, stock, SKU).
* Check imported products in the product listing page.
* Configure webhooks to receive notifications for specific events.

---

## **Example CSV Format**

```csv
title,description,price,stock,sku
Laptop,High-performance gaming laptop,1500,10,LAP123
Keyboard,Mechanical keyboard,100,25,KEY456
Mouse,Wireless mouse,50,40,MOU789
```

---

## **Key Learnings / Skills Demonstrated**

* Handling file uploads in Django using forms and templates.
* Reading and processing CSV files with Python.
* CRUD operations in Django models.
* Implementing webhook notifications via HTTP requests.
* Structuring Django projects with multiple apps.
* Using Git for version control and branch management.

---

## **Contact / Author**

**Eswar Chandra Yadlapalli**

* Email: [eswarchandrayadlapalli@gmail.com](mailto:eswarchandrayadlapalli@gmail.com)

---
