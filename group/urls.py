from django.contrib import admin
from django.urls import include,path
from group import views
urlpatterns = [
    path('add/',views.add),
    path('contactUs/',views.contactUs),
    path('',views.index),
    path('aboutUs/',views.aboutUs),
]