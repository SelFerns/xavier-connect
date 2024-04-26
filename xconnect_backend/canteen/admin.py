from django.contrib import admin
from .models import Menu, Cart, Items, Order, Payment


class ItemsInline(admin.TabularInline):
    model = Items
    extra = 1  # Number of empty forms to display


class ItemsAdmin(admin.ModelAdmin):
    inlines = [ItemsInline]


admin.site.register(Menu)
admin.site.register(Cart, ItemsAdmin)
admin.site.register(Items)
admin.site.register(Order)
admin.site.register(Payment)
