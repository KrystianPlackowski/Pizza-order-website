from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:menu_id>", views.item_info, name="item_info"),
    path("add", views.add_to_cart, name="add_to_cart"),
    path("cart", views.cart, name="cart"),
    path("order", views.place_order, name="place_order"),
]
