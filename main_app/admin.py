from django.contrib import admin
from .models import Product, Category, Tag, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'categories', 'is_deleted']
    search_fields = ['name', 'description']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'date_created']
    list_filter = ['date_created']
    inlines = [OrderItemInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
