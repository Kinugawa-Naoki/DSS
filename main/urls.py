from django.urls.conf import include
from django.urls import path, include
from .views import deliverable_updatefunc, indexfunc, createfunc, deliverable_listfunc, deliverable_detailfunc, deliverable_deletefunc

urlpatterns = [
    path('account/', include('main.account.urls')),
    path('', indexfunc, name='index'),
    path('create/', createfunc, name='create'),
    path('deliverable_list/', deliverable_listfunc, name='deliverable_list'),
    path('deliverable_detail/<int:pk>/', deliverable_detailfunc, name='deliverable_detail'),
    path('deliverable_update/<int:pk>/', deliverable_updatefunc, name='deliverable_update'),
    path('deliverable_delete/<int:pk>/', deliverable_deletefunc, name='deliverable_delete'),
]