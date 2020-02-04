from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from collections import defaultdict
from nested_dict import nested_dict
from ordered_set import OrderedSet

from .models import Menu, Topping, Order, Dish

# Create your views here.
def index(request):
    menu = Menu.objects.all()
    menu_nameset = defaultdict(OrderedSet)
    menu_pricedict = nested_dict()
    for item in menu:
        menu_nameset[item.kind].add(item.name)
        menu_pricedict[item.kind][item.size][item.name] = item.price

    class foodtable:
        def __init__(self, name, columns, body):
            self.name = name
            self.columns = columns
            self.body = body
    
    def prepare_table(kind: str, columns):
        body = []
        for name in menu_nameset[kind]:
            row = []
            row.append(name)
            for size in columns:
                row.append(menu_pricedict[kind][size][name])
            body.append(row)
        return foodtable(kind.capitalize(), columns, body)

    regular_pizza = prepare_table("regular pizza", ['Small', 'Large'])
    silician_pizza = prepare_table("silician pizza", ['Small', 'Large'])
    subs = prepare_table("sub", ['Small', 'Large'])
    pasta = prepare_table("pasta", [''])
    salads = prepare_table("salad", [''])
    platters = prepare_table("dinner platter", ['Small', 'Large'])

    context = {
        "menu": [regular_pizza, silician_pizza, subs, pasta, salads, platters],
        "toppings": Topping.objects.all(),
    }
    return render(request, "orders/index.html", context)
