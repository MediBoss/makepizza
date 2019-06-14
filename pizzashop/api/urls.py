from django.urls import path

from .views import PizzaList, PizzaDetail

urlpatterns = [
    path('pizza/', PizzaList.as_view(), name='pizza_list'),
    path('pizza/<int:pk>/', PizzaDetail.as_view(), name="pizza_detail")
]
