from .models import Cart, Category

def cart_counter(request):
    cart_count = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_count = cart.total_items
        except Cart.DoesNotExist:
            pass
    return {'cart_count': cart_count}

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}
