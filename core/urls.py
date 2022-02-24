from django.contrib import admin
from django.urls import include,path
from .views import UserLogin
from .views import UserLogout


urlpatterns = [
    path('login/',UserLogin.as_view(), name = 'login'),
    path('logout/',UserLogout.as_view(), name = 'logout')


]