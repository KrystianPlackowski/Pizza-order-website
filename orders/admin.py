from django.contrib import admin

from .models import Topping, ItemKind, ItemName, ItemSize, Menu
# Register your models here.

admin.site.register(Topping)
admin.site.register(ItemKind)
admin.site.register(ItemName)
admin.site.register(ItemSize)
admin.site.register(Menu)
