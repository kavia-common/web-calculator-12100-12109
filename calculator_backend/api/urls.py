from django.urls import path
from .views import health, add, subtract, multiply, divide

urlpatterns = [
    path('health/', health, name='Health'),
    path('add/', add, name='Add'),
    path('subtract/', subtract, name='Subtract'),
    path('multiply/', multiply, name='Multiply'),
    path('divide/', divide, name='Divide'),
]
