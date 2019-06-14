from rest_framework import serializers

from pizza.models import Pizza, Topping, PizzaOrder

class ToppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topping
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):

    toppins = ToppingSerializer(many=True, required=False)
    class Meta:
        model = Pizza
        fields = '__all__'