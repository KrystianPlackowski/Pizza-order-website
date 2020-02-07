from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.defaulttags import register
from django.core.exceptions import ObjectDoesNotExist

from .models import Topping, ItemKind, ItemName, ItemSize, MenuItem

@register.filter
def get_size(instance, key):
    try:
        result = instance.get(size_parent=key)
    except ObjectDoesNotExist:
        result = ""
    return result

# Create your views here.
def index(request):
    context = {
        "kinds": ItemKind.objects.all(),
        "toppings": Topping.objects.all(),
    }
    return render(request, "orders/index.html", context)

def item_info(request, menu_id):
    item = MenuItem.objects.get(id=menu_id)
    context = {"item": item}
    return render(request, "orders/item_info.html", context)
