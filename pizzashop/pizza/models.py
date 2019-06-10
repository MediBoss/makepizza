from django.db import models

class Topping(models.Model):
    pass

class PizzaTopping(models.Model):
    topping = models.ForeignKey('Topping', on_delete=models.PROTECT)
    pizza = models.ForeignKey('Pizza', on_delete=models.PROTECT)

class Pizza(models.Model):
    
    name = models.CharField(max_length=60)
    toppings = models.ForeignKey('Topping', through=PizzaTopping)

    def __str__(self):
        return self.name