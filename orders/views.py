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
    if 'pizza' in item.kind:
        selected_toppings = request.session['selected_toppings']
        if request.method == 'POST':
            new_topping = request.POST.get('topping', None)
            toDelete_topping = request.POST.get('delete', None)

            # Avoid readding/redeleting the same topping if user refreshed the page
            if new_topping and not new_topping in selected_toppings: 
                selected_toppings.append(new_topping)
            elif toDelete_topping and toDelete_topping in selected_toppings:
                selected_toppings.remove(toDelete_topping)
        else:
            selected_toppings = []
        request.session['selected_toppings'] = selected_toppings
        request.session.modified = True

        def numberOfToppingsToName(kind, x):
            if x > 3:
                return 'Special'
            if kind == 'regular pizza':
                return {0: 'Cheese', 1: '1 topping', 2: '2 toppings', 3: '3 toppings'}[x]
            elif kind == 'silician pizza':
                return {0: 'Cheese', 1: '1 item', 2: '2 items', 3: '3 items'}[x]
            else:
                raise Http404('Behaviour not implemented for this kind of pizza.')

        def filterMenuByProperties(kind, name, size):
            try:
                kind_parent = ItemKind.objects.filter(kind=kind).first()
                name_parent = ItemName.objects.filter(name=name, kind_parent=kind_parent).first()
                size_parent = ItemSize.objects.filter(size=size, kind_parent=kind_parent).first()
                return MenuItem.objects.filter(name_parent=name_parent, size_parent=size_parent).first()
            except:
                return None

        item = filterMenuByProperties(
                kind = item.kind,
                name = numberOfToppingsToName(item.kind, len(selected_toppings)),
                size = item.size
                )
        
        new_size = request.POST.get('size', None)
        if new_size:
            item = filterMenuByProperties(kind=item.kind, name=item.name, size=new_size)

        if not item:
            raise Http404('Item with selected properties in form not found in menu.')

        context = {
            "size": new_size,
            "item": item,
            "selected_toppings": selected_toppings, 
            "not_selected_toppings": Topping.objects.exclude(name__in=selected_toppings).all(),
        }
        return render(request, "orders/item_info.html", context)
    else:
        return render(request, "orders/error.html", context={"message": "Currently not supported."})

def add_to_cart(request, menu_id):
    return render(request, "orders/error.html", context={"message": "Currently not implemented."})
