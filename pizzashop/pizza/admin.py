from django.contrib import admin
from pizza.models import Pizza, PizzaOrder, Topping


# Register your models here.
admin.site.register(Pizza)
admin.site.register(PizzaOrder)
admin.site.register(Topping)