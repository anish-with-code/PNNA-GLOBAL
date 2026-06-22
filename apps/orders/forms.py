from django import forms
from .models import Order
from apps.users.models import Address


class CheckoutForm(forms.Form):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('upi', 'UPI'),
        ('net_banking', 'Net Banking'),
        ('cod', 'Cash on Delivery'),
    ]

    shipping_address = forms.ModelChoiceField(
        queryset=Address.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Shipping Address'
    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Payment Method'
    )
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Order notes (optional)'}),
        label='Additional Notes'
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shipping_address'].queryset = Address.objects.filter(user=user)
