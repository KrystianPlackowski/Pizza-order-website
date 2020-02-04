from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("add/<int:menu_id>", views.dish, name="make_dish"),
    #path("login", views.login_view, name="login"),
    #path("logout", views.logout_view, name="logout")
]
