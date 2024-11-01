# Storefront
A simple application that is made in Django

## Development Setup (python)
Use `python v3.11`
```sh
python -m venv venv
source venv/scripts/activate
pip install -r requirements.txt
```

## Django Project
```sh
django-admin
django-admin startproject storefront .
django-admin startapp playground
```

### Run Application
```sh
python manage.py runserver
```

### Models
```sh
python manage.py startapp store
python manage.py startapp tags
```

#### Migration
```sh
python manage.py migrate

python manage.py makemigrations
python manage.py migrate
```

#### ORM
##### Demo
```sh
python manage.py shell
```
```sh
from store.models import Product

# get all products
Product.objects.all()

# create new product
product = Product()
product.name = "Demo"
product.description = "Demo description"
product.price = 12.19

product.save()
```