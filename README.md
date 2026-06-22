# PNNA GLOBAL E-Commerce Website

A modern, responsive e-commerce website for PNNA Global luxury fashion jewellery.

## Features

✨ **Modern Design**
- Luxury gold and black theme
- Responsive layout for all devices
- Smooth animations and transitions

🛍️ **Shopping Features**
- Product grid with filtering (Western/Ethnic/Best Sellers)
- Search functionality
- Product quick view modal
- Add to cart with quantity control
- Persistent cart storage (localStorage)

💳 **Checkout**
- Direct WhatsApp integration
- One-click checkout to WhatsApp
- Order summary with totals

📱 **Mobile Responsive**
- Works perfectly on all screen sizes
- Mobile-optimized navigation
- Touch-friendly buttons

## Getting Started

### Quick Start
1. Open `index.html` in a web browser
2. Browse products and add to cart
3. Click the checkout button to order via WhatsApp

### File Structure
```
project/
├── index.html       # Main HTML file
├── style.css        # All styling
├── script.js        # JavaScript functionality
└── README.md        # This file
```

## How to Use

### Browsing Products
- Click **Filter buttons** (All Products, Western, Ethnic, Best Sellers)
- Use **Search bar** to find specific products
- Click **View** on any product to see details

### Shopping
1. Click **Add Cart** to add products to your cart
2. View your cart by clicking the shopping cart icon
3. Adjust quantities with +/- buttons
4. Remove items as needed

### Checkout
1. Click **Proceed to WhatsApp** button
2. Confirm your order in WhatsApp
3. Get WhatsApp response from PNNA Global

## Product Information

**Total Products**: 20 premium earrings

**Categories**:
- **Western**: Modern, stylish earrings for contemporary look
- **Ethnic**: Traditional Indian designs (Jhumka, Chandbali)

**Price Range**: ₹160 - ₹439

**All products include**:
- Free delivery across India
- Prices inclusive of all taxes
- Best discounts (up to 50% OFF)

## Contact

📱 **WhatsApp**: +91 73595 08044
📷 **Instagram**: @pnnaglobal
🌐 **Website**: pnna-global.netlify.app

## Features Explained

### Search
Real-time product search by name or category

### Filters
- All Products
- Western (Modern earrings)
- Ethnic (Traditional designs)
- Best Sellers (Most popular items)

### Product Details Modal
Click "View" to see:
- High-resolution product image
- Full product description
- Original and discounted prices
- Discount percentage

### Shopping Cart
- Add/remove items
- Adjust quantities
- See live total
- Cart persists even after closing browser

### WhatsApp Integration
- Automatic order message generation
- Pre-filled with product details and prices
- Direct link to WhatsApp

## Browser Support

Works on all modern browsers:
- Chrome
- Firefox
- Safari
- Edge
- Mobile browsers

## Customization

### Adding New Products
Edit `script.js` and add to the `products` array:
```javascript
{
    id: 21,
    name: "Product Name",
    category: "western" or "ethnic",
    type: "hot-seller", "best-seller", "new-arrival", "best-value",
    price: 299,
    mrp: 599,
    discount: 50,
    image: "image-url",
    description: "Product description"
}
```

### Changing Colors
Edit color variables in `style.css`:
- Primary Gold: `#d4af37`
- Dark Background: `#2c2c2c`
- Accent Red: `#ff6b6b`

## Tips

✅ **Best Seller Products** are marked with special badges
✅ **Huge Discounts** - Most products 40-50% OFF
✅ **Free Delivery** across India
✅ **Fast Ordering** - Direct WhatsApp checkout

## Performance

- Fast loading with optimized assets
- Smooth animations at 60fps
- Responsive design loads quickly on mobile
- Cart data persists using browser storage

## License

© 2024 PNNA Global. All rights reserved.
