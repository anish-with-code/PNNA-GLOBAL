// PNNA Global - JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips and popovers
    initializeBootstrapComponents();

    // Add event listeners
    setupEventListeners();
});

function initializeBootstrapComponents() {
    // Tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
}

function setupEventListeners() {
    // Product image carousel
    setupImageCarousel();

    // Add to cart form submission
    setupAddToCart();

    // Wishlist toggle
    setupWishlistToggle();

    // Search form
    setupSearchForm();

    // Quantity input
    setupQuantityInput();
}

function setupImageCarousel() {
    const thumbnails = document.querySelectorAll('.img-thumbnail');
    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            const carousel = bootstrap.Carousel.getInstance(document.querySelector('#productImageCarousel'));
            if (carousel) {
                const index = Array.from(thumbnails).indexOf(this);
                carousel.to(index);
            }
        });
    });
}

function setupAddToCart() {
    const cartForms = document.querySelectorAll('form[action*="add-to-cart"]');
    cartForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Adding...';
            }
        });
    });
}

function setupWishlistToggle() {
    const wishlistBtns = document.querySelectorAll('a[href*="add-to-wishlist"]');
    wishlistBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (this.closest('form')) return; // Skip if it's a form

            e.preventDefault();

            const url = this.href;
            const icon = this.querySelector('i');

            fetch(url, {
                headers: {'X-Requested-With': 'XMLHttpRequest'}
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Toggle heart icon
                    if (icon.classList.contains('bi-heart')) {
                        icon.classList.remove('bi-heart');
                        icon.classList.add('bi-heart-fill');
                    } else {
                        icon.classList.add('bi-heart');
                        icon.classList.remove('bi-heart-fill');
                    }

                    // Show toast notification
                    showNotification('Updated!', 'Wishlist updated successfully');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
}

function setupSearchForm() {
    const searchInput = document.querySelector('input[placeholder*="Search"]');
    if (searchInput) {
        searchInput.addEventListener('keyup', debounce(function(e) {
            // Optional: Auto-search as user types
        }, 300));
    }
}

function setupQuantityInput() {
    const quantityInputs = document.querySelectorAll('input[name="quantity"]');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            // Ensure valid quantity
            let value = parseInt(this.value);
            if (isNaN(value) || value < 1) {
                this.value = 1;
            }
            if (value > parseInt(this.max)) {
                this.value = this.max;
            }
        });
    });
}

function showNotification(title, message) {
    // Create a simple notification
    const notification = document.createElement('div');
    notification.className = 'alert alert-success alert-dismissible fade show position-fixed';
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; max-width: 300px;';
    notification.innerHTML = `
        <strong>${title}</strong> ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    document.body.appendChild(notification);

    // Auto-remove after 3 seconds
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Price formatting
function formatPrice(price) {
    return '₹' + parseFloat(price).toFixed(2);
}

// Calculate cart totals
function calculateCartTotal() {
    const items = document.querySelectorAll('tr[data-product-id]');
    let total = 0;

    items.forEach(item => {
        const price = parseFloat(item.querySelector('[data-price]').textContent);
        const quantity = parseInt(item.querySelector('input[name="quantity"]').value);
        total += price * quantity;
    });

    return total;
}

// Filter products by category
function filterProductsByCategory(category) {
    const products = document.querySelectorAll('[data-category]');
    products.forEach(product => {
        if (category === 'all' || product.dataset.category === category) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
}

// Sort products
function sortProducts(sortBy) {
    const container = document.querySelector('[data-products-container]');
    if (!container) return;

    const products = Array.from(container.querySelectorAll('[data-product]'));

    products.sort((a, b) => {
        let aValue, bValue;

        switch(sortBy) {
            case 'price_low':
                aValue = parseFloat(a.dataset.price);
                bValue = parseFloat(b.dataset.price);
                return aValue - bValue;
            case 'price_high':
                aValue = parseFloat(a.dataset.price);
                bValue = parseFloat(b.dataset.price);
                return bValue - aValue;
            case 'newest':
                aValue = new Date(a.dataset.created);
                bValue = new Date(b.dataset.created);
                return bValue - aValue;
            case 'rating':
                aValue = parseFloat(a.dataset.rating);
                bValue = parseFloat(b.dataset.rating);
                return bValue - aValue;
            default:
                return 0;
        }
    });

    // Re-render products
    container.innerHTML = '';
    products.forEach(product => {
        container.appendChild(product);
    });
}

// Smooth scroll to element
function smoothScroll(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return false;

    return form.checkValidity() === false ? false : true;
}

// Mobile menu toggle
function toggleMobileMenu() {
    const navbar = document.querySelector('.navbar-collapse');
    if (navbar) {
        navbar.classList.toggle('show');
    }
}

// Price range slider
function setupPriceRangeSlider() {
    const minInput = document.querySelector('input[name="min_price"]');
    const maxInput = document.querySelector('input[name="max_price"]');

    if (minInput && maxInput) {
        [minInput, maxInput].forEach(input => {
            input.addEventListener('change', function() {
                if (parseInt(minInput.value) > parseInt(maxInput.value)) {
                    const temp = minInput.value;
                    minInput.value = maxInput.value;
                    maxInput.value = temp;
                }
            });
        });
    }
}

// Print order
function printOrder() {
    window.print();
}

// Copy order number
function copyOrderNumber() {
    const orderNumber = document.querySelector('[data-order-number]');
    if (orderNumber) {
        const text = orderNumber.textContent;
        navigator.clipboard.writeText(text).then(() => {
            showNotification('Copied!', 'Order number copied to clipboard');
        });
    }
}
