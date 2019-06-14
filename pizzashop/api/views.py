from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Pizza, Topping
from .serializers import PizzaSerializer, ToppingSerializer



class PizzaList(APIView):
    
    def get(self, request):
        ''' API Endpoint that allows pizza models to be viewed '''

        pizzas = Pizza.objects.all()
        data = PizzaSerializer(pizzas, many=True).data
        return Response(data)

class PizzaDetail(APIView):

    def get(self, request, pk):

        pizza = get_object_or_404(Pizza, pk=pk)
        data = PizzaSerializer(pizza).data

        return Response(data)

