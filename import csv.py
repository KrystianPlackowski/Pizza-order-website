#!/usr/bin/env python
import os
import sys
from pizza.settings import *
import django
from django.conf import settings
from django.db import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza.settings")
django.setup()

from orders.models import Topping, ItemKind, ItemName, ItemSize, MenuItem

everything = MenuItem.objects.all()
print(everything)
