from main.models import DeliverableInfo
from os import name
from django.urls import path
from .views import createfunc, deliverable_listfunc, signupfunc, loginfunc, deliverable_detailfunc

urlpatterns = [
    path('signup', signupfunc, name='signup'),
    path('login', loginfunc, name='login'),
    path('create', createfunc, name='create'),
    path('deliverable_list', deliverable_listfunc, name='deliverable_list'),
    path('deliverable_dtail/<int:pk>', deliverable_detailfunc, name='deliverable_detail'),
]