from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price', 'get_total']
    fields = ['product', 'quantity', 'price', 'get_total']

    def get_total(self, obj):
        return obj.get_total


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'total_amount', 'status', 'payment_status', 'created_at']
    list_filter = ['status', 'payment_status', 'created_at', 'payment_method']
    search_fields = ['order_number', 'user__email', 'tracking_number']
    readonly_fields = ['order_number', 'created_at', 'updated_at', 'subtotal']
    inlines = [OrderItemInline]

    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'created_at', 'updated_at')
        }),
        ('Shipping Details', {
            'fields': ('shipping_address', 'tracking_number', 'delivered_at')
        }),
        ('Payment', {
            'fields': ('payment_method', 'payment_status', 'subtotal', 'shipping_cost', 'tax', 'total_amount')
        }),
        ('Order Status', {
            'fields': ('status', 'notes')
        }),
    )

    actions = ['mark_confirmed', 'mark_shipped', 'mark_delivered', 'mark_cancelled']

    def mark_confirmed(self, request, queryset):
        queryset.update(status='confirmed')

    def mark_shipped(self, request, queryset):
        queryset.update(status='shipped')

    def mark_delivered(self, request, queryset):
        from django.utils import timezone
        queryset.update(status='delivered', delivered_at=timezone.now())

    def mark_cancelled(self, request, queryset):
        queryset.update(status='cancelled')

    mark_confirmed.short_description = "Mark as Confirmed"
    mark_shipped.short_description = "Mark as Shipped"
    mark_delivered.short_description = "Mark as Delivered"
    mark_cancelled.short_description = "Mark as Cancelled"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'get_total']
    list_filter = ['order__created_at', 'product']
    search_fields = ['order__order_number', 'product__name']
    readonly_fields = ['order', 'product', 'quantity', 'price', 'get_total']

    def get_total(self, obj):
        return obj.get_total
    get_total.short_description = 'Total Price'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
