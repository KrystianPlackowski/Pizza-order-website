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
    kind_parent = models.ForeignKey(ItemKind, on_delete=models.CASCADE, related_name="name_list", verbose_name='Kind', default=-1)
    name = models.CharField(max_length=64, blank=False, default='')

    def __str__(self):
        return f"({self.kind_parent.kind}) - {self.name}"

    def kind(self):
        return self.kind_parent.kind

class ItemSize(models.Model):
    kind_parent = models.ForeignKey(ItemKind, on_delete=models.CASCADE, related_name="size_list", verbose_name='Kind', default=-1)
    size = models.CharField(max_length=64, blank=False, default='')

    def __str__(self):
        return f"({self.kind_parent.kind}) - {self.size}"

    def kind(self):
        return self.kind_parent.kind

class MenuItem(models.Model):
    name_parent = models.ForeignKey(ItemName, on_delete=models.CASCADE, related_name='item_list', verbose_name='(Kind) - Name', default=-1)
    size_parent = models.ForeignKey(ItemSize, on_delete=models.CASCADE, related_name='item_list', verbose_name='(Kind) - Size', default=-1)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, default=0)

    def __str__(self):
        return f"({self.id}) - {self.name_parent.kind_parent.kind} - {self.name_parent.name} - {self.size_parent.size} - {self.price}$"

    def kind(self):
        return self.name_parent.kind_parent.kind

    def name(self):
        return self.name_parent.name

    def size(self):
        return self.size_parent.size

