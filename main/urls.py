from main.models import DeliverableInfo
from os import name
from django.urls import path
from .views import createfunc, signupfunc, loginfunc, deliverable_detailfunc

urlpatterns = [
    path('signup', signupfunc, name='signup'),
    path('login', loginfunc, name='login'),
    path('', createfunc, name='main'),
    path('', deliverable_detailfunc, name='deliverable_detail'),
]