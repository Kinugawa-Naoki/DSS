from django.urls.conf import include
from django.urls import path, include
from .views import indexfunc, createfunc, deliverable_listfunc, deliverable_detailfunc

urlpatterns = [
    path('account/', include('main.account.urls')),
    path('', indexfunc, name='index'),
    path('create/', createfunc, name='create'),
    path('deliverable_list/', deliverable_listfunc, name='deliverable_list'),
    path('deliverable_detail/<int:pk>', deliverable_detailfunc, name='deliverable_detail'),
]