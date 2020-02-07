from django.contrib import admin

from .models import Topping, ItemKind, ItemName, ItemSize, MenuItem
# Register your models here.

admin.site.register(Topping)
admin.site.register(ItemKind)
admin.site.register(ItemName)
admin.site.register(ItemSize)
admin.site.register(MenuItem)
