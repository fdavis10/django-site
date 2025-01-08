from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInInline]