from django.contrib import admin

from order.models import ShopCart, Order, OrderDetail


class ShopcartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')


class DetailInline(admin.TabularInline):
    model= OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'city', 'phone', 'total', 'status')
    list_filter = ('status', 'create_at')



class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'total', 'update_at')



admin.site.register(Order, OrderAdmin)
admin.site.register(ShopCart, ShopcartAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)