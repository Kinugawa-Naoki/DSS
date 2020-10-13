from os import name
from django.urls import path
from .views import createfunc

urlpatterns = [
    path('', createfunc, name='main'),
]