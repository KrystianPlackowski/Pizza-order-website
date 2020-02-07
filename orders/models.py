from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=64, blank=False, default='')

    def __str__(self):
        return f"{self.name}"

class ItemKind(models.Model):
    kind = models.CharField(max_length=64, blank=False, default='')

    def __str__(self):
        return f"{self.kind}"

class ItemName(models.Model):
    kind_id = models.ForeignKey(ItemKind, on_delete=models.CASCADE, related_name="name_list")
    name = models.CharField(max_length=64, blank=False, default='')

    def __str__(self):
        return f"{self.kind_id} - {self.name}"

class ItemSize(models.Model):
    name_id = models.ForeignKey(ItemName, on_delete=models.CASCADE, related_name="size_list")
    size = models.CharField(max_length=64, blank=False, default='')

    def __str__(self):
        return f"{self.name_id} - {self.size}"


class Menu(models.Model):
    size_id = models.ForeignKey(ItemSize, on_delete=models.CASCADE, related_name='element', default=-1)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=False, default=0)

    def __str__(self):
        return f"{self.id} - {self.size_id} - {self.price}"


