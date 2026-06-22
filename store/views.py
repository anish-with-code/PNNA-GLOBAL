from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import uuid

from .models import Category, Product, ProductImage, Cart, CartItem, Order, OrderItem, Wishlist
from .forms import (
    UserRegistrationForm, UserLoginForm, SearchForm, AddToCartForm,
    CheckoutForm, ContactForm
)

def home(request):
    featured_products = Product.objects.filter(is_featured=True, status='available')[:6]
    bestsellers = Product.objects.filter(is_bestseller=True, status='available')[:6]
    new_products = Product.objects.filter(is_new=True, status='available')[:6]
    categories = Category.objects.all()

    context = {
        'featured_products': featured_products,
        'bestsellers': bestsellers,
        'new_products': new_products,
        'categories': categories,
    }
    return render(request, 'store/home.html', context)

def products(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    sort = request.GET.get('sort', '')

    products_list = Product.objects.filter(status='available')

    if query:
        products_list = products_list.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    if category:
        products_list = products_list.filter(category__slug=category)

    if min_price:
        try:
            products_list = products_list.filter(price__gte=float(min_price))
        except ValueError:
            pass

    if max_price:
        try:
            products_list = products_list.filter(price__lte=float(max_price))
        except ValueError:
            pass

    if sort == 'price_low':
        products_list = products_list.order_by('price')
    elif sort == 'price_high':
        products_list = products_list.order_by('-price')
    elif sort == 'newest':
        products_list = products_list.order_by('-created_at')
    elif sort == 'rating':
        products_list = products_list.order_by('-rating')

    paginator = Paginator(products_list, 12)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)

    categories = Category.objects.all()
    search_form = SearchForm(initial={
        'q': query,
        'category': category,
        'min_price': min_price,
        'max_price': max_price,
        'sort': sort,
    })

    context = {
        'products': products,
        'categories': categories,
        'search_form': search_form,
        'query': query,
        'total_count': paginator.count,
    }
    return render(request, 'store/products.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()
    related_products = Product.objects.filter(
        category=product.category,
        status='available'
    ).exclude(pk=product.pk)[:4]

    add_to_cart_form = AddToCartForm()

    context = {
        'product': product,
        'images': images,
        'related_products': related_products,
        'add_to_cart_form': add_to_cart_form,
    }
    return render(request, 'store/product_detail.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            Cart.objects.create(user=user)
            Wishlist.objects.create(user=user)
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!')
                    return redirect(request.GET.get('next', 'home'))
                else:
                    messages.error(request, 'Invalid password.')
            except User.objects.DoesNotExist:
                messages.error(request, 'Email not found.')
    else:
        form = UserLoginForm()

    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

@login_required
def profile(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'cart': cart,
        'wishlist': wishlist,
        'orders': orders,
    }
    return render(request, 'store/profile.html', context)

@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            try:
                cart = Cart.objects.get(user=request.user)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(user=request.user)

            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={'quantity': quantity}
            )

            if not created:
                if cart_item.quantity + quantity <= product.stock:
                    cart_item.quantity += quantity
                    cart_item.save()
                else:
                    messages.error(request, 'Not enough stock available.')
                    return redirect('product_detail', slug=slug)
            elif quantity > product.stock:
                messages.error(request, 'Not enough stock available.')
                cart_item.delete()
                return redirect('product_detail', slug=slug)

            messages.success(request, f'{product.name} added to cart!')
            return redirect('cart')
    else:
        form = AddToCartForm()

    return redirect('product_detail', slug=slug)

@login_required
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity <= 0:
            cart_item.delete()
            messages.success(request, 'Item removed from cart.')
        elif quantity <= cart_item.product.stock:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated.')
        else:
            messages.error(request, 'Not enough stock available.')

    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'{product_name} removed from cart.')
    return redirect('cart')

@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return redirect('cart')

    if not cart.items.exists():
        messages.error(request, 'Your cart is empty.')
        return redirect('cart')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"
            order.total_amount = cart.total_price
            order.save()

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
                item.product.stock -= item.quantity
                item.product.save()

            cart.items.all().delete()

            messages.success(request, f'Order placed successfully! Order number: {order.order_number}')
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm(initial={
            'full_name': f"{request.user.first_name} {request.user.last_name}".strip(),
            'email': request.user.email,
        })

    context = {
        'form': form,
        'cart': cart,
    }
    return render(request, 'store/checkout.html', context)

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_confirmation.html', {'order': order})

@login_required
def add_to_wishlist(request, slug):
    product = get_object_or_404(Product, slug=slug)

    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.info(request, f'{product.name} removed from wishlist.')
    else:
        wishlist.products.add(product)
        messages.success(request, f'{product.name} added to wishlist!')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})

    return redirect('product_detail', slug=slug)

@login_required
def wishlist_view(request):
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)

    return render(request, 'store/wishlist.html', {'wishlist': wishlist})

def categories(request):
    categories_list = Category.objects.all()
    paginator = Paginator(categories_list, 12)
    page = request.GET.get('page', 1)
    categories = paginator.get_page(page)

    return render(request, 'store/categories.html', {'categories': categories})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products_list = Product.objects.filter(category=category, status='available')

    paginator = Paginator(products_list, 12)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)

    context = {
        'category': category,
        'products': products,
        'total_count': paginator.count,
    }
    return render(request, 'store/category_products.html', context)

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'store/contact.html', {'form': form})

from django.contrib.auth.models import User
