from django.db import models

# Create your models here.
class Menu(models.Model):
    kind = models.CharField(max_length=64, blank=False, default='')
    name = models.CharField(max_length=64, blank=False, default='')
    size = models.CharField(max_length=64, blank=True, default='')
    toppings_amount = models.CharField(max_length=64, blank=True, default='')
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=False, default=0)

    def __str__(self):
        result = f"({self.kind}) {self.name}"
        if self.size != '':
            result += f" - {self.size}"
        if self.toppings_amount != '':
            result += f" - {self.toppings_amount}"
        return result + f" - {self.price} $"

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

class Topping(models.Model):
    name = models.CharField(max_length=64, blank=False, default='')

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    def __str__(self):
        if len(self.dish_list.all()) == 0:
            return f"{self.id} - empty order"
        else:
            dish_list = ", ".join(str(seg) for seg in self.dish_list.all())
            return f"{self.id} - ({dish_list})"

class Dish(models.Model):
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="dishes_containing")
    toppings_list = models.ManyToManyField(Topping, blank=True, related_name="toppings")
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="dish_list")

    def __str__(self):
        if len(self.toppings_list.all()) == 0:
            return f"{self.menu_item}"
        else:
            toppings_list = ", ".join(str(seg) for seg in self.toppings_list.all())
            return f"{self.menu_item} with ({toppings_list})"

    class Meta:
        verbose_name_plural = 'Dishes'
