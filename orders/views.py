from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.urls import reverse
from django.template.defaulttags import register
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

from .models import Topping, ItemKind, ItemName, ItemSize, MenuItem, Dish, Order

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
    if not item:
        raise Http404('Item not in menu.')

    if 'pizza' in item.kind:
        selected_toppings = request.session.get('selected_toppings', [])
        if request.method == 'POST':
            new_topping = request.POST.get('topping', None)
            toDelete_topping = request.POST.get('delete', None)
            if new_topping:
                new_topping = int(new_topping)
            if toDelete_topping:
                toDelete_topping = int(toDelete_topping)

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
            if kind == 'silician pizza':
                return {0: 'Cheese', 1: '1 item', 2: '2 items', 3: '3 items'}[x]
            else:
                return {0: 'Cheese', 1: '1 topping', 2: '2 toppings', 3: '3 toppings'}[x]

        item = MenuItem.objects.filter(
                name_parent__kind_parent__kind = item.kind,
                name_parent__name = numberOfToppingsToName(item.kind, len(selected_toppings)),
                size_parent__size = item.size
                ).first()

        new_size = request.POST.get('size', None)
        if item and new_size:
             item = MenuItem.objects.filter(
                    name_parent__kind_parent__kind = item.kind,
                    name_parent__name = item.name,
                    size_parent__size = new_size
                    ).first()

        if not item:
            raise Http404('Item with selected properties in form not found in menu.\
                    Or name/number of toppings with undefined behaviour assinged to pizza. \
                    Default is: 0 toppings -> name=\'Cheese\', 1 topping -> name=\'1 topping\', \
                    2 toppings -> name=\'2 toppings\', 3 toppings -> name=\'3 toppings\', \
                    4 or 5 toppings -> name=\'Special\'')

        context = {
            "item": item,
            "selected_toppings": Topping.objects.filter(id__in=selected_toppings), 
            "not_selected_toppings": Topping.objects.exclude(id__in=selected_toppings).all(),
        }
        return render(request, "orders/item_info.html", context)
    else:
        return render(request, "orders/error.html", context={"message": "Currently not supported."})

@require_http_methods(["POST"])
def add_to_cart(request):
    menu_id = request.POST.get('cart_item', None)
    if menu_id:
        item = MenuItem.objects.get(id=int(menu_id))
    if not menu_id or not item:
        raise Http404('Item not in menu.')
    selected_toppings = request.session.get('selected_toppings', [])

    new_dish = Dish(item_parent=item)
    new_dish.save()
    new_dish.toppings.add(*[topping for topping in selected_toppings])
    dishes = request.session.get('users_dishes', [])
    dishes.append(new_dish.id)
    request.session['users_dishes'] = dishes

    return render(request, "orders/success.html", context={"message": "Successfully added to cart!"})

def cart(request):
    dishes = request.session.get('users_dishes', [])
    toDelete_dish = request.POST.get('delete', None)
    if toDelete_dish:
        toDelete_dish = int(toDelete_dish)
    if toDelete_dish and toDelete_dish in dishes:
        dishes.remove(toDelete_dish)
        Dish.objects.filter(id=toDelete_dish).delete()
    
    context = {
        "dishes": Dish.objects.filter(id__in=dishes).all(),
        "overall_price": Dish.objects \
            .filter(id__in=dishes) \
            .aggregate(overall_price=Sum('item_parent__price'))['overall_price'],
    }
    return render(request, "orders/cart.html", context)

@require_http_methods(["POST"])
def place_order(request):
    return render(request, "orders/error.html", context={"message": "Currently not implemented"})
