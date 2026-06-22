const products = [
    {
        id: 1,
        name: "Pearl & Black Crystal Drop Earrings",
        category: "western",
        type: "hot-seller",
        price: 199,
        mrp: 399,
        discount: 50,
        image: "https://via.placeholder.com/300x300?text=Pearl+Black+Crystal",
        description: "Elegant pearl and black crystal drop earrings with premium craftsmanship."
    },
    {
        id: 2,
        name: "Gold Flower Tassel Drop Earrings",
        category: "western",
        type: "best-seller",
        price: 240,
        mrp: 449,
        discount: 47,
        image: "https://via.placeholder.com/300x300?text=Gold+Flower+Tassel",
        description: "Beautiful gold flower design with elegant tassel detailing."
    },
    {
        id: 3,
        name: "Royal Lavender Ghungroo Earrings",
        category: "ethnic",
        type: "new-arrival",
        price: 349,
        mrp: 599,
        discount: 42,
        image: "https://via.placeholder.com/300x300?text=Lavender+Ghungroo",
        description: "Traditional ghungroo earrings with royal lavender stone setting."
    },
    {
        id: 4,
        name: "4-Style Earring Combo Pack",
        category: "western",
        type: "best-value",
        price: 439,
        mrp: 799,
        discount: 45,
        image: "https://via.placeholder.com/300x300?text=4+Style+Combo",
        description: "Get 4 different earring styles in one amazing combo pack."
    },
    {
        id: 5,
        name: "White Butterfly Rhinestone Studs",
        category: "western",
        price: 199,
        mrp: 349,
        discount: 43,
        image: "https://via.placeholder.com/300x300?text=White+Butterfly",
        description: "Delicate white butterfly studs with sparkling rhinestones."
    },
    {
        id: 6,
        name: "Gold Arc Crystal Stud Earrings",
        category: "western",
        price: 199,
        mrp: 349,
        discount: 43,
        image: "https://via.placeholder.com/300x300?text=Gold+Arc+Crystal",
        description: "Modern arc design with crystal embellishments."
    },
    {
        id: 7,
        name: "Pearl Wing Ear Cuff Earrings",
        category: "western",
        price: 199,
        mrp: 349,
        discount: 43,
        image: "https://via.placeholder.com/300x300?text=Pearl+Wing+Cuff",
        description: "Trendy ear cuff design with pearl and wing motifs."
    },
    {
        id: 8,
        name: "Silver Arch Chandbali - Turquoise",
        category: "ethnic",
        price: 280,
        mrp: 499,
        discount: 44,
        image: "https://via.placeholder.com/300x300?text=Turquoise+Chandbali",
        description: "Elegant silver arch chandbali with vibrant turquoise stone."
    },
    {
        id: 9,
        name: "Silver Arch Chandbali - Red",
        category: "ethnic",
        price: 280,
        mrp: 499,
        discount: 44,
        image: "https://via.placeholder.com/300x300?text=Red+Chandbali",
        description: "Classic silver arch chandbali with deep red stone."
    },
    {
        id: 10,
        name: "Silver Arch Chandbali - Green",
        category: "ethnic",
        price: 280,
        mrp: 499,
        discount: 44,
        image: "https://via.placeholder.com/300x300?text=Green+Chandbali",
        description: "Beautiful silver arch chandbali with green stone."
    },
    {
        id: 11,
        name: "Silver Arch Chandbali - Black",
        category: "ethnic",
        price: 280,
        mrp: 499,
        discount: 44,
        image: "https://via.placeholder.com/300x300?text=Black+Chandbali",
        description: "Sophisticated silver arch chandbali with black stone."
    },
    {
        id: 12,
        name: "Silver Arch Chandbali - Lavender",
        category: "ethnic",
        price: 280,
        mrp: 499,
        discount: 44,
        image: "https://via.placeholder.com/300x300?text=Lavender+Chandbali",
        description: "Elegant silver arch chandbali with lavender stone."
    },
    {
        id: 13,
        name: "Silver Arch Chandbali - Maroon",
        category: "ethnic",
        price: 280,
        mrp: 499,
        discount: 44,
        image: "https://via.placeholder.com/300x300?text=Maroon+Chandbali",
        description: "Rich silver arch chandbali with maroon stone."
    },
    {
        id: 14,
        name: "Antique Pink Jhumka Earrings",
        category: "ethnic",
        type: "best-seller",
        price: 299,
        mrp: 549,
        discount: 46,
        image: "https://via.placeholder.com/300x300?text=Pink+Jhumka",
        description: "Traditional jhumka earrings with antique pink finish."
    },
    {
        id: 15,
        name: "Purple Bow Heart Drop Earrings",
        category: "western",
        type: "new-arrival",
        price: 160,
        mrp: 299,
        discount: 47,
        image: "https://via.placeholder.com/300x300?text=Purple+Bow+Heart",
        description: "Cute purple bow-shaped heart drop earrings."
    },
    {
        id: 16,
        name: "White Floral Hoop Crystal Drop",
        category: "western",
        type: "hot",
        price: 220,
        mrp: 399,
        discount: 45,
        image: "https://via.placeholder.com/300x300?text=Floral+Hoop+Crystal",
        description: "Stunning white floral hoop design with crystal drops."
    },
    {
        id: 17,
        name: "Silver Black Onyx Elephant Chandbali",
        category: "ethnic",
        type: "best-seller",
        price: 199,
        mrp: 399,
        discount: 50,
        image: "https://via.placeholder.com/300x300?text=Onyx+Elephant",
        description: "Unique elephant motif chandbali with black onyx stone."
    },
    {
        id: 18,
        name: "Antique Gold Ruby Jhumka Earrings",
        category: "ethnic",
        type: "best-seller",
        price: 359,
        mrp: 599,
        discount: 40,
        image: "https://via.placeholder.com/300x300?text=Ruby+Jhumka",
        description: "Luxurious antique gold jhumka with ruby stone setting."
    },
    {
        id: 19,
        name: "Black Rose Gold Bow Drop Earrings",
        category: "western",
        type: "new-arrival",
        price: 199,
        mrp: 349,
        discount: 43,
        image: "https://via.placeholder.com/300x300?text=Rose+Gold+Bow",
        description: "Trendy black and rose gold bow drop earrings."
    },
    {
        id: 20,
        name: "Antique Gold Turquoise Jhumka",
        category: "ethnic",
        type: "new-arrival",
        price: 350,
        mrp: 599,
        discount: 42,
        image: "https://via.placeholder.com/300x300?text=Turquoise+Jhumka",
        description: "Elegant antique gold jhumka with turquoise gemstone."
    }
];

let cart = [];
let filteredProducts = [...products];
let currentFilter = 'all';

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    renderProducts(products);
    loadCartFromStorage();
});

// Render products
function renderProducts(productsToShow) {
    const grid = document.getElementById('productsGrid');
    grid.innerHTML = '';

    if (productsToShow.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; padding: 40px; color: #999;">No products found</p>';
        return;
    }

    productsToShow.forEach(product => {
        const badge = product.type ? product.type.replace('-', ' ').toUpperCase() : '';
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
            <div class="product-image">
                <img src="${product.image}" alt="${product.name}">
                ${badge ? `<div class="product-badge">${badge}</div>` : ''}
            </div>
            <div class="product-info">
                <div class="product-category">${product.category}</div>
                <div class="product-name">${product.name}</div>
                <div class="product-prices">
                    <span class="product-price">₹${product.price}</span>
                    <span class="product-original">₹${product.mrp}</span>
                    <span class="product-discount">${product.discount}% OFF</span>
                </div>
                <div class="product-actions">
                    <button class="view-btn" onclick="viewProduct(${product.id})">View</button>
                    <button class="add-btn" onclick="addToCart(${product.id})">Add Cart</button>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });
}

// Filter products
function filterProducts(filter) {
    currentFilter = filter;

    // Update active button
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');

    if (filter === 'all') {
        filteredProducts = [...products];
    } else if (filter === 'bestseller') {
        filteredProducts = products.filter(p => p.type && p.type.includes('best-seller'));
    } else {
        filteredProducts = products.filter(p => p.category === filter);
    }

    renderProducts(filteredProducts);
}

// Search products
document.getElementById('searchInput').addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    const results = products.filter(p =>
        p.name.toLowerCase().includes(query) ||
        p.category.toLowerCase().includes(query)
    );
    renderProducts(results);
});

// View product details
function viewProduct(productId) {
    const product = products.find(p => p.id === productId);
    if (!product) return;

    document.getElementById('modalImage').src = product.image;
    document.getElementById('modalTitle').textContent = product.name;
    document.getElementById('modalCategory').textContent = product.category.toUpperCase();
    document.getElementById('modalPrice').textContent = product.price;
    document.getElementById('modalMRP').textContent = product.mrp;
    document.getElementById('modalDiscount').textContent = product.discount;
    document.getElementById('modalDescription').textContent = product.description;

    document.getElementById('productModal').classList.add('active');
    document.body.style.overflow = 'hidden';

    // Store current product for modal add to cart
    window.currentProduct = product;
}

// Close modal
function closeModal() {
    document.getElementById('productModal').classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Close modal when clicking outside
document.getElementById('productModal').addEventListener('click', (e) => {
    if (e.target.id === 'productModal') {
        closeModal();
    }
});

// Add to cart from modal
function addFromModal() {
    if (window.currentProduct) {
        addToCart(window.currentProduct.id);
        closeModal();
    }
}

// Add to cart
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (!product) return;

    const existingItem = cart.find(item => item.id === productId);

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            ...product,
            quantity: 1
        });
    }

    saveCartToStorage();
    updateCartUI();
    showNotification('Added to cart!');
}

// Update cart UI
function updateCartUI() {
    const cartCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    document.querySelector('.cart-count').textContent = cartCount;

    const cartItemsContainer = document.getElementById('cartItems');
    const cartTotal = document.getElementById('cartTotal');

    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<p class="empty-cart">Your cart is empty</p>';
        cartTotal.textContent = '0';
        return;
    }

    cartItemsContainer.innerHTML = cart.map(item => `
        <div class="cart-item">
            <div class="cart-item-image" style="background: url('${item.image}') center/cover;"></div>
            <div class="cart-item-info">
                <div class="cart-item-name">${item.name}</div>
                <div class="cart-item-price">₹${item.price} × ${item.quantity}</div>
                <div class="cart-item-qty">
                    <button class="qty-btn" onclick="updateQuantity(${item.id}, -1)">−</button>
                    <span>${item.quantity}</span>
                    <button class="qty-btn" onclick="updateQuantity(${item.id}, 1)">+</button>
                    <button class="remove-btn" onclick="removeFromCart(${item.id})">Remove</button>
                </div>
            </div>
        </div>
    `).join('');

    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    cartTotal.textContent = total;
}

// Update quantity
function updateQuantity(productId, change) {
    const item = cart.find(i => i.id === productId);
    if (!item) return;

    item.quantity += change;

    if (item.quantity <= 0) {
        removeFromCart(productId);
    } else {
        saveCartToStorage();
        updateCartUI();
    }
}

// Remove from cart
function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    saveCartToStorage();
    updateCartUI();
}

// Toggle cart sidebar
function toggleCart() {
    document.getElementById('cartSidebar').classList.toggle('active');
}

// Checkout via WhatsApp
function checkout() {
    if (cart.length === 0) {
        alert('Your cart is empty!');
        return;
    }

    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

    let message = '🎁 *PNNA GLOBAL - ORDER* 🎁\n\n';
    message += '*Products:*\n';

    cart.forEach(item => {
        message += `• ${item.name} (x${item.quantity})\n  Price: ₹${item.price} each\n`;
    });

    message += `\n*Total: ₹${total}*\n`;
    message += `\nPlease confirm this order. Thank you! 😊`;

    const whatsappNumber = '917359508044';
    const encodedMessage = encodeURIComponent(message);
    const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodedMessage}`;

    window.open(whatsappUrl, '_blank');
}

// Save cart to localStorage
function saveCartToStorage() {
    localStorage.setItem('pnnaCart', JSON.stringify(cart));
}

// Load cart from localStorage
function loadCartFromStorage() {
    const saved = localStorage.getItem('pnnaCart');
    if (saved) {
        cart = JSON.parse(saved);
        updateCartUI();
    }
}

// Show notification
function showNotification(message) {
    const notif = document.createElement('div');
    notif.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #2c2c2c;
        color: white;
        padding: 15px 20px;
        border-radius: 5px;
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    notif.textContent = message;
    document.body.appendChild(notif);

    setTimeout(() => {
        notif.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notif.remove(), 300);
    }, 2000);
}

// CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(400px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(400px); opacity: 0; }
    }
`;
document.head.appendChild(style);
