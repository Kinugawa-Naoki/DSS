from django.urls import path
from .views import signupfunc, loginfunc, logoutfunc, termsfunc

urlpatterns = [
    path('', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('terms/', termsfunc, name='terms'),
]
