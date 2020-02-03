from django.contrib import admin

from .models import Menu, Topping, Dish, Order
# Register your models here.
admin.site.register(Menu)
admin.site.register(Topping)
admin.site.register(Dish)
admin.site.register(Order)
