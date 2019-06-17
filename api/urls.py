from django.urls import path

from .views import PizzaViewSet


urlpatterns = [
    path('<int:pk>/', PizzaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('', PizzaViewSet.as_view({'get': 'list', 'post': 'create'})),
]