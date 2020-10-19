from django.urls import path
from .views import signupfunc, loginfunc, logoutfunc

urlpatterns = [
    path('', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
]
