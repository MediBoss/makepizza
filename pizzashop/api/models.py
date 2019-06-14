from django.db import models


class PizzaOrder(models.Model):
    topping = models.ForeignKey('Topping', on_delete=models.PROTECT)
    pizza = models.ForeignKey('Pizza', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.pizza.name} with {self.topping.name}"



class Pizza(models.Model):
    ''' Pizza Model that defines basic representation of a Pizza'''
    
    PIZZA_SIZES = (
        (12, '12 inches'),
        (15, '15 inches'),
        (18, '18 inches'),
    )

    name = models.CharField(max_length=60)
    toppings = models.ManyToManyField('Topping', through=PizzaOrder) # pizza can have many topings, so can toppings
    price_small = models.DecimalField(max_digits=8, decimal_places=2)
    price_medium = models.DecimalField(max_digits=8, decimal_places=2)
    price_large = models.DecimalField(max_digits=8, decimal_places=2)
    descprition = models.TextField(null=True)

    def __str__(self):
        return f"{self.name} Pizza with toppinps {self.toppings}"

class Topping(models.Model):
    name = models.CharField(max_length=60)
    on_top_of = models.ManyToManyField('Pizza', through=PizzaOrder)

    def __str__(self):
        return f"{self.name} topping"
