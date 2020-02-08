#!/usr/bin/env python
import os
import sys
from pizza.settings import *
import django
from django.conf import settings
from django.db import models

import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza.settings")
django.setup()

from orders.models import Topping, ItemKind, ItemName, ItemSize, MenuItem

with open('menu_tables.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    ItemKind.objects.all().delete()

    print("Inserting menu tables data...\n")
    for kind, name, size, price in csv_reader:
        kind_parent = ItemKind.objects.filter(kind=kind).first()
        if not kind_parent:
            kind_parent = ItemKind(kind=kind)
            kind_parent.save()

        name_parent = ItemName.objects.filter(kind_parent=kind_parent, name=name).first()
        if not name_parent:
            name_parent = ItemName(kind_parent=kind_parent, name=name)
            name_parent.save()

        size_parent = ItemSize.objects.filter(kind_parent=kind_parent, size=size).first()
        if not size_parent:
            size_parent = ItemSize(kind_parent=kind_parent, size=size)
            size_parent.save()

        item = MenuItem(name_parent=name_parent, size_parent=size_parent, price=price)
        item.save()
        print("inserted:", item)

with open('menu_toppings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    Topping.objects.all().delete()

    print("\nInserting menu toppings data...\n")
    for topping in csv_reader:
        topping = Topping(name=topping[0])
        topping.save()
        print("inserted:", topping)
