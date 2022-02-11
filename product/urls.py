from django.contrib import admin
from django.urls import include,path
from product import views

urlpatterns = [
    path('addproduct/',views.addProduct),
    path('view/',views.viewproduct),
    path('productpage/',views.productpage),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('help/',views.help),


]
