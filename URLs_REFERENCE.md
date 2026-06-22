# PNNA Global - Website URLs Reference

Access all pages and features using these URLs after running `python manage.py runserver`

---

## 🏠 Main Pages

| Feature | URL | Description |
|---------|-----|-------------|
| Homepage | http://localhost:8000/ | Main landing page with featured products |
| Products | http://localhost:8000/products/ | Browse all products with search & filters |
| Categories | http://localhost:8000/categories/ | View all product categories |
| About | http://localhost:8000/about/ | About PNNA Global |
| Contact | http://localhost:8000/contact/ | Contact form & support |

---

## 👤 User Authentication

| Feature | URL | Description |
|---------|-----|-------------|
| Register | http://localhost:8000/register/ | Create new account |
| Login | http://localhost:8000/login/ | Login to account |
| Logout | http://localhost:8000/logout/ | Logout from account |
| Profile | http://localhost:8000/profile/ | View user profile & orders |

---

## 🛍️ Shopping Features

| Feature | URL | Method | Description |
|---------|-----|--------|-------------|
| View Cart | http://localhost:8000/cart/ | GET | View shopping cart |
| Add to Cart | http://localhost:8000/add-to-cart/<slug>/ | POST | Add product to cart |
| Update Cart | http://localhost:8000/cart/update/<id>/ | POST | Update item quantity |
| Remove from Cart | http://localhost:8000/cart/remove/<id>/ | GET | Remove item from cart |
| Checkout | http://localhost:8000/checkout/ | GET/POST | Checkout page |

---

## ❤️ Wishlist

| Feature | URL | Method | Description |
|---------|-----|--------|-------------|
| View Wishlist | http://localhost:8000/wishlist/ | GET | View saved items |
| Add to Wishlist | http://localhost:8000/add-to-wishlist/<slug>/ | GET/POST | Add product to wishlist |

---

## 📦 Product Pages

| Feature | URL | Description |
|---------|-----|-------------|
| Product Detail | http://localhost:8000/product/<slug>/ | View product details |
| By Category | http://localhost:8000/category/<slug>/ | View products in category |

---

## 📋 Orders

| Feature | URL | Description |
|---------|-----|-------------|
| Order Confirmation | http://localhost:8000/order-confirmation/<id>/ | View order details |
| Order History | http://localhost:8000/profile/ | View all orders in profile |

---

## 👨‍💼 Admin Panel

| Feature | URL | Username | Description |
|---------|-----|----------|-------------|
| Admin Home | http://localhost:8000/admin/ | (superuser) | Admin dashboard |
| All Products | http://localhost:8000/admin/store/product/ | (superuser) | Manage products |
| Add Product | http://localhost:8000/admin/store/product/add/ | (superuser) | Create new product |
| Categories | http://localhost:8000/admin/store/category/ | (superuser) | Manage categories |
| Orders | http://localhost:8000/admin/store/order/ | (superuser) | View & manage orders |
| Users | http://localhost:8000/admin/auth/user/ | (superuser) | Manage users |
| Product Images | http://localhost:8000/admin/store/productimage/ | (superuser) | Manage product images |

---

## 🔍 Search & Filter URLs

### Search Products
```
http://localhost:8000/products/?q=earrings
```

### Filter by Category
```
http://localhost:8000/products/?category=western
```

### Filter by Price
```
http://localhost:8000/products/?min_price=100&max_price=400
```

### Sort Products
```
http://localhost:8000/products/?sort=price_low
```

Options: `price_low`, `price_high`, `newest`, `rating`

### Combined Filters
```
http://localhost:8000/products/?q=earrings&category=ethnic&sort=price_low
```

---

## 📱 Sample Product URLs

### Specific Products
```
http://localhost:8000/product/pearl-black-crystal-drop-earrings/
http://localhost:8000/product/gold-flower-tassel-drop-earrings/
http://localhost:8000/product/antique-gold-ruby-jhumka-earrings/
http://localhost:8000/product/silver-arch-chandbali-turquoise/
```

### By Category
```
http://localhost:8000/category/western/
http://localhost:8000/category/ethnic/
```

---

## 🛠️ Management Commands

### In Terminal/Command Prompt

```bash
# Create admin user
python manage.py createsuperuser

# Load all 20 products
python manage.py populate_products

# Database migrations
python manage.py migrate

# Create backups
python manage.py dumpdata > backup.json

# Restore from backup
python manage.py loaddata backup.json

# Django shell
python manage.py shell

# Check for issues
python manage.py check

# Collect static files (production)
python manage.py collectstatic --noinput

# Clear cache
python manage.py clear_cache
```

---

## 🌐 Query Parameters Guide

### Search Parameters
- `q` - Search query (e.g., `?q=earrings`)
- `category` - Category slug (e.g., `?category=ethnic`)
- `min_price` - Minimum price (e.g., `?min_price=100`)
- `max_price` - Maximum price (e.g., `?max_price=500`)
- `sort` - Sort by field (e.g., `?sort=price_low`)
- `page` - Page number (e.g., `?page=2`)

### Example URLs
```
?q=jhumka&category=ethnic&sort=price_high&page=1
?min_price=200&max_price=300&sort=newest
?q=earrings&sort=rating&page=1
```

---

## 📊 Admin Features

### Product Management
1. **Add Product**
   - Name, slug, category
   - Description
   - Price, MRP
   - Stock quantity
   - Status (available/out_of_stock/discontinued)
   - Mark as featured, bestseller, new

2. **Upload Images**
   - Multiple images per product
   - Set primary image
   - Add alt text for SEO

3. **Categories**
   - Create categories
   - Add descriptions
   - Auto-generated slugs

4. **Orders**
   - View all orders
   - Update status
   - Track deliveries
   - View customer details

5. **Users**
   - Manage user accounts
   - View user profiles
   - Edit user information

---

## 🚀 Testing Checklist

Use these URLs to test all features:

- [ ] Homepage loads: `/`
- [ ] Products page: `/products/`
- [ ] Search works: `/products/?q=earrings`
- [ ] Category filter: `/products/?category=western`
- [ ] Product details: `/product/pearl-black-crystal-drop-earrings/`
- [ ] Register: `/register/`
- [ ] Login: `/login/`
- [ ] Add to cart: Works from product page
- [ ] View cart: `/cart/`
- [ ] Wishlist: `/wishlist/`
- [ ] Profile: `/profile/`
- [ ] Checkout: `/checkout/`
- [ ] Admin: `/admin/`
- [ ] About: `/about/`
- [ ] Contact: `/contact/`

---

## 📞 Support URLs

### External Links (Integrated)
- WhatsApp: https://wa.me/917359508044
- Instagram: https://instagram.com/pnnaglobal
- Email: info@pnnaglobal.com

### In-App Links
- WhatsApp button in navbar
- Instagram link in footer
- Contact form: `/contact/`
- Support info: `/about/`

---

## 🔐 Admin Login Steps

1. Go to http://localhost:8000/admin/
2. Enter username: (as created during `createsuperuser`)
3. Enter password: (as created during `createsuperuser`)
4. Click "Log in"

After login, you can:
- Add/edit/delete products
- Manage inventory
- View orders
- Manage users
- Upload images

---

## 💡 Tips

### URLs to Bookmark
- **Homepage**: http://localhost:8000/
- **Admin**: http://localhost:8000/admin/
- **Products**: http://localhost:8000/products/

### Quick Admin Actions
- Add product: `/admin/store/product/add/`
- View orders: `/admin/store/order/`
- Manage categories: `/admin/store/category/`
- View users: `/admin/auth/user/`

### Test Accounts
Create test accounts by:
1. Going to `/register/`
2. Filling in test details
3. Confirming email (auto in development)
4. Login with test credentials

---

## 🚨 Common Issues & Solutions

### Issue: 404 Page Not Found
- Check URL spelling
- Ensure server is running
- Try hard refresh (Ctrl+Shift+R)

### Issue: Admin page shows no data
- Make sure migrations are applied: `python manage.py migrate`
- Load products: `python manage.py populate_products`

### Issue: Static files (CSS/JS) not loading
- Run: `python manage.py collectstatic --noinput`
- Reload page (Ctrl+Shift+R)

### Issue: Images not showing
- Upload images in admin panel
- Check permissions on media folder
- Verify file paths in templates

---

## 📝 Notes

- All URLs are case-sensitive
- Slugs use hyphens (e.g., `pearl-earrings`)
- GET request URLs can be accessed directly
- POST request URLs need form submission
- Admin panel requires login
- Some pages require authentication

---

## 🎯 Production URLs

When deployed, replace `localhost:8000` with:
- Your domain: `https://yourdomain.com`
- Railway: `https://your-app.railway.app`
- Render: `https://your-app.onrender.com`

All URLs will work the same way!

---

**Happy browsing! 🎉**

For more help, see COMPLETE_SETUP.md or QUICK_START.md
