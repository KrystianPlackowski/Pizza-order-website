from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from collections import defaultdict, namedtuple
from ordered_set import OrderedSet

from .models import Menu, Topping, Order, Dish

# Create your views here.
def index(request):
    menu_xlabels = defaultdict(OrderedSet)
    menu_ylabels = defaultdict(OrderedSet)
    menu_itemdict = dict()
    for item in Menu.objects.all():
        menu_xlabels[item.kind].add(item.size)
        menu_ylabels[item.kind].add(item.name)
        menu_itemdict[(item.kind, item.size, item.name)] = item
    
    # Note: each row of each table consists first of one string type value (this is row's label),
    # then multiple Menu.objects type values
    def prepare_table(kind: str):
        body = []
        for name in menu_ylabels[kind]:
            row = [name]
            for size in menu_xlabels[kind]:
                if (kind, size, name) in menu_itemdict.keys():
                    row.append(menu_itemdict[(kind, size, name)])
                else:
                    row.append('')
            body.append(row)
        foodtable = namedtuple('foodtable', ['name', 'xlabels', 'body'])
        return foodtable(kind.capitalize(), list(menu_xlabels[kind]), body)

    context = {
        "menu": [prepare_table(kind) for kind in menu_xlabels.keys()],
        "toppings": Topping.objects.all(),
    }
    return render(request, "orders/index.html", context)

def item_info(request, menu_id):
    item = Menu.objects.get(id=menu_id)
    context = {"item": item}
    return render(request, "orders/item_info.html", context)
