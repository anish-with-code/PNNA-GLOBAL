# PNNA Global - E-Commerce Platform

A modern, fully responsive e-commerce website for luxury fashion jewelry built with Django, Bootstrap 5, and modern web technologies.

## Features

### 1. **Homepage**
- Attractive hero carousel banner
- Featured products section
- Best sellers showcase
- New arrivals
- Categories section
- Mobile responsive design
- Quick links to WhatsApp and Instagram

### 2. **Product System**
- Product name, price, and description
- Multiple product images with carousel
- Category filtering
- Stock quantity management
- Add to cart functionality
- Wishlist button
- Product ratings and reviews
- Search and filter capabilities

### 3. **User System**
- User registration with email
- Login and logout functionality
- User profile page
- Order history tracking
- Wishlist management
- Account information

### 4. **Shopping Features**
- Shopping cart with add/remove/update items
- Real-time quantity updates
- Cart total calculation
- Comprehensive checkout page
- Order confirmation page
- Free delivery across India

### 5. **Admin Panel**
- Secure admin login (Django admin)
- Dashboard with statistics
- Add, edit, and delete products
- Upload multiple product images per product
- Manage categories
- Manage users
- Manage orders and order status
- Inventory management
- Beautiful admin interface with filters and search

### 6. **Database**
- SQLite (production-ready with PostgreSQL support)
- Models: Category, Product, ProductImage, Cart, CartItem, Order, OrderItem, Wishlist
- Proper relationships and constraints
- Database indexing for performance

### 7. **Extra Features**
- Pagination (12 items per page)
- Product search with autocomplete
- Advanced filters (category, price range, rating, sort)
- Contact page
- About page
- FAQ section
- SEO-friendly URLs
- Error handling and validation
- Loading animations
- Responsive design for all devices

## Project Structure

```
ecommerce/
├── ecommerce/              # Main Django project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── store/                 # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Django forms
│   ├── urls.py            # App URL configuration
│   ├── admin.py           # Admin configuration
│   └── management/        # Management commands
│       └── commands/
│           └── populate_products.py
├── templates/             # HTML templates
│   └── store/
│       ├── base.html      # Base template
│       ├── home.html      # Homepage
│       ├── products.html  # Products listing
│       ├── product_detail.html
│       ├── cart.html
│       ├── checkout.html
│       ├── order_confirmation.html
│       ├── profile.html
│       ├── wishlist.html
│       ├── register.html
│       ├── login.html
│       ├── about.html
│       ├── contact.html
│       └── categories.html
├── static/                # Static files
│   ├── css/
│   │   └── style.css      # Custom CSS
│   └── js/
│       └── script.js      # JavaScript
├── media/                 # Media uploads
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment

### Step 1: Clone/Extract the Project

```bash
cd ~/Desktop/project
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
# Follow the prompts to create admin account
```

### Step 6: Populate Products

```bash
python manage.py populate_products
```

This command adds all 20 PNNA Global jewelry products to the database from the PDF catalog.

### Step 7: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 8: Run Development Server

```bash
python manage.py runserver
```

The website will be available at: **http://localhost:8000**

Admin panel: **http://localhost:8000/admin**

## Admin Credentials

- Username: (as set during superuser creation)
- Password: (as set during superuser creation)

## Key URLs

| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/products/` | All products |
| `/product/<slug>/` | Product detail |
| `/register/` | User registration |
| `/login/` | User login |
| `/profile/` | User profile |
| `/cart/` | Shopping cart |
| `/checkout/` | Checkout page |
| `/wishlist/` | Wishlist |
| `/categories/` | All categories |
| `/category/<slug>/` | Category products |
| `/about/` | About page |
| `/contact/` | Contact page |
| `/admin/` | Admin panel |

## Models & Database Schema

### Category
- name (CharField)
- slug (SlugField)
- description (TextField)

### Product
- name (CharField)
- slug (SlugField)
- category (ForeignKey)
- product_type (CharField: western/ethnic)
- description (TextField)
- price (DecimalField)
- mrp (DecimalField)
- stock (IntegerField)
- status (CharField: available/out_of_stock/discontinued)
- is_featured (BooleanField)
- is_bestseller (BooleanField)
- is_new (BooleanField)
- rating (FloatField)
- created_at, updated_at (DateTimeField)

### ProductImage
- product (ForeignKey)
- image (ImageField)
- alt_text (CharField)
- is_primary (BooleanField)

### Cart & CartItem
- cart linked to user
- items with product, quantity
- automatic total calculation

### Order & OrderItem
- order_number (unique)
- user (ForeignKey)
- delivery details
- total_amount
- status tracking
- items list

### Wishlist
- user (OneToOneField)
- products (ManyToManyField)

## Features Implemented

✅ Responsive Bootstrap 5 design
✅ Product search and filtering
✅ Pagination (12 items per page)
✅ User authentication system
✅ Shopping cart management
✅ Order checkout and confirmation
✅ Admin panel with full CRUD operations
✅ Wishlist functionality
✅ Multiple product images
✅ Stock management
✅ Order tracking
✅ Contact form
✅ About page
✅ FAQ section
✅ Mobile navigation
✅ Loading animations
✅ Form validation
✅ Error handling
✅ SEO-friendly URLs
✅ Free delivery messaging
✅ WhatsApp integration links

## Technologies Used

- **Backend**: Django 5.0.1
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite3 (included)
- **Form Styling**: Django Crispy Forms
- **Image Processing**: Pillow
- **Web Server**: Gunicorn (production-ready)

## Configuration Files

### .env (Environment Variables)
```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### settings.py
- Debug mode
- Static files configuration
- Media files configuration
- Template configuration
- Database configuration
- Installed apps
- Middleware

## API Endpoints (Future Enhancement)

The application is ready for REST API implementation using Django REST Framework.

## Performance Optimizations

- Database indexing on frequently queried fields
- Static file compression with WhiteNoise
- Image optimization with Pillow
- Pagination to reduce page load
- Caching ready (Django cache framework)
- CDN ready for static files

## Security Features

- CSRF protection
- XSS prevention
- SQL injection prevention (Django ORM)
- Secure password hashing
- Session security
- CORS configuration
- Input validation
- Form validation

## SEO Features

- Meta tags
- Semantic HTML
- Sitemap ready
- robots.txt ready
- Clean URLs (slugs)
- Mobile-friendly
- Fast loading times

## Deployment

### Production Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Update `SECRET_KEY` with a strong random key
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL database (optional)
- [ ] Configure static files CDN
- [ ] Set up proper logging
- [ ] Enable HTTPS
- [ ] Configure email backend
- [ ] Set up backups

### Deploy to Heroku

```bash
pip install gunicorn
heroku login
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Deploy to AWS/GCP

Use appropriate deployment guides for your chosen platform.

## Support & Contact

- **WhatsApp**: +91 73595 08044
- **Instagram**: @pnnaglobal
- **Email**: info@pnnaglobal.com
- **Website**: www.pnna-global.netlify.app

## License

This project is proprietary to PNNA Global. All rights reserved.

## Author

Created for PNNA Global - Premium Luxury Fashion Jewelry

---

**Last Updated**: June 2024
**Version**: 1.0.0
