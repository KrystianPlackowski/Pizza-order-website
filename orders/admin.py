from django.contrib import admin

from .models import Topping, ItemKind, ItemName, ItemSize, MenuItem, Dish, Order
# Register your models here.

class ItemKindAdmin(admin.ModelAdmin):
    list_display = ("kind",)

class ItemNameAdmin(admin.ModelAdmin):
    list_display = ("kind", "name")
    search_fields = ("kind_parent__kind", "name")

class ItemSizeAdmin(admin.ModelAdmin):
    list_display = ("kind", "size")
    search_fields = ("kind_parent__kind", "size")

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("kind", "name", "size", "price")
    search_fields = ("name_parent__kind_parent__kind", "name_parent__name", "size_parent__size", "price")

    """def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "name_parent":
            kwargs["queryset"] = ItemName.objects.filter(kind_parent__kind='sub')
        if db_field.name == "size_parent":
            kwargs["queryset"] = ItemSize.objects.filter(kind_parent__kind='sub')
        return super(MenuItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    """
    #fields = ("name_parent", "size_parent", "price")

admin.site.register(Topping)
admin.site.register(ItemKind, ItemKindAdmin)
admin.site.register(ItemName, ItemNameAdmin)
admin.site.register(ItemSize, ItemSizeAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Dish)
admin.site.register(Order)
