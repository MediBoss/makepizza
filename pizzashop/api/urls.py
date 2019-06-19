from django.urls import path

# from .views import PizzaList, PizzaDetail
from rest_framework import routers
from api.views import PizzaViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()

router.register(r'pizza', PizzaViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'auth', include('rest_framework.urls'))
]
