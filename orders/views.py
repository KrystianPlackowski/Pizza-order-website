from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from collections import defaultdict, namedtuple
from ordered_set import OrderedSet

from .models import Topping, ItemKind, ItemName, ItemSize, Menu

# Create your views here.
def index(request):
    context = {
        "kinds": ItemKind.objects.all(),
        "toppings": Topping.objects.all(),
    }
    return render(request, "orders/index.html", context)

def item_info(request, menu_id):
    item = Menu.objects.get(id=menu_id)
    context = {"item": item}
    return render(request, "orders/item_info.html", context)
