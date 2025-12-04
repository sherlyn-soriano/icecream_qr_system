from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.resgiter(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_active")
    list_filter = ("is_active",)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "payment_method", "total_amount")
    inlines =   [OrderItemInline]