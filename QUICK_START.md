# PNNA Global - Quick Start Guide

Get the e-commerce platform up and running in 5 minutes!

## 🚀 Quick Start (Windows)

### 1. Open Command Prompt/PowerShell

```bash
cd C:\Users\YourUsername\Desktop\project
```

### 2. Activate Virtual Environment

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Admin Account

```bash
python manage.py createsuperuser
```
Follow the prompts:
- Username: admin
- Email: admin@pnnaglobal.com
- Password: (enter your password)

### 6. Add Products

```bash
python manage.py populate_products
```

### 7. Run Server

```bash
python manage.py runserver
```

### 8. Access the Website

- **Frontend**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

---

## 🚀 Quick Start (macOS/Linux)

### 1. Open Terminal

```bash
cd ~/Desktop/project
```

### 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Admin Account

```bash
python manage.py createsuperuser
```

### 6. Add Products

```bash
python manage.py populate_products
```

### 7. Run Server

```bash
python manage.py runserver
```

### 8. Access the Website

- **Frontend**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

---

## 📱 Test the Website

### Create a Test Account

1. Go to http://localhost:8000/register
2. Fill in the form with test details
3. Click "Register"

### Login

1. Go to http://localhost:8000/login
2. Use your registered email and password

### Browse Products

1. Click "Products" in navigation
2. Use filters and search
3. Click on any product to see details

### Add to Cart

1. On product page, select quantity
2. Click "Add to Cart"
3. Go to cart: http://localhost:8000/cart

### Checkout

1. Click "Proceed to Checkout"
2. Fill in delivery details
3. Click "Place Order"
4. See confirmation with order number

### Admin Panel

1. Go to http://localhost:8000/admin
2. Login with superuser credentials
3. Add products manually if needed
4. Upload product images
5. Manage orders and users

---

## 🎨 Customize the Website

### Change Colors

Edit `static/css/style.css`:
```css
:root {
    --primary-color: #d4203c;  /* Change this to your brand color */
    --secondary-color: #667eea;
}
```

### Add Your Logo

1. Replace the navbar brand text in `templates/store/base.html`:
```html
<a class="navbar-brand fw-bold" href="{% url 'home' %}">
    <i class="bi bi-gem"></i> YOUR BRAND NAME
</a>
```

### Change Site Title

Edit `ecommerce/settings.py`:
```python
SITE_NAME = "Your Store Name"
```

### Add Product Images

1. Login to admin at /admin/
2. Go to "Products"
3. Click a product
4. Scroll to "Product images" section
5. Click "Add another Product Image"
6. Upload image and mark as primary if first image

---

## 🔧 Troubleshooting

### Virtual Environment Not Activating

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Port 8000 Already in Use

```bash
python manage.py runserver 8001
# Then access at http://localhost:8001
```

### Database Errors

```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading

```bash
python manage.py collectstatic --noinput
```

### Module Not Found Error

```bash
pip install --upgrade -r requirements.txt
```

---

## 📚 Common Commands

```bash
# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Create new app
python manage.py startapp appname

# Make migrations for model changes
python manage.py makemigrations

# Open Django shell
python manage.py shell

# Clear cache
python manage.py clear_cache

# Populate demo products
python manage.py populate_products
```

---

## 🌐 Connect to Services

### WhatsApp Integration

Edit `templates/store/base.html` and update phone number:
```html
<a href="https://wa.me/917359508044" target="_blank">
    WhatsApp
</a>
```

### Instagram Integration

Update Instagram handle in footer and contact pages.

---

## 📊 Database Backup

### Backup SQLite Database

```bash
# Windows
copy db.sqlite3 db.sqlite3.backup

# macOS/Linux
cp db.sqlite3 db.sqlite3.backup
```

### Restore from Backup

```bash
# Windows
copy db.sqlite3.backup db.sqlite3

# macOS/Linux
cp db.sqlite3.backup db.sqlite3
```

---

## 🚀 Deployment

### Deploy to Heroku (Free Tier Deprecated)

Use alternatives like:
- Railway.app
- Render.com
- PythonAnywhere
- AWS Elastic Beanstalk

### Deploy to Railway.app

1. Create account at railway.app
2. Connect GitHub repo
3. Set environment variables
4. Deploy with one click

---

## 💡 Tips & Tricks

### Development Mode

```bash
# Enable debug for better error messages
DEBUG = True  # in settings.py
```

### Create Dummy User

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
User.objects.create_user('testuser', 'test@example.com', 'password123')
```

### Empty Database (Fresh Start)

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_products
```

---

## 📞 Support

- **WhatsApp**: +91 73595 08044
- **Instagram**: @pnnaglobal
- **Email**: info@pnnaglobal.com

---

**Happy Coding! 🎉**
