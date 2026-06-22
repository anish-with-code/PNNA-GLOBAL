from .models import Cart


def cart_context(request):
    if request.user.is_authenticated:
        try:
            cart = request.user.cart
            return {
                'cart': cart,
                'cart_item_count': cart.get_cart_item_count,
                'cart_total': cart.get_cart_total,
            }
        except Cart.DoesNotExist:
            return {'cart': None, 'cart_item_count': 0, 'cart_total': 0}
    return {'cart': None, 'cart_item_count': 0, 'cart_total': 0}
