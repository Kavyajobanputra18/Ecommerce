from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def add(request):
    return HttpResponse("group called...")

#Create views of Contact us page
def contactUs(request):
    context ={
        'contact_name' :['Dhiraj','Suresh','Vinay','Ajay','Rohan'],
    }
    return render(request, 'group/contactUs.html',context)

#Create views of index  page
def index(request):
    context ={
        'name' : 'FLIPKART',
    }
    return render(request, 'group/index.html',context)

#Create views of About us page
def aboutUs(request):
    context ={
        'isActive' :False,
        'age' : 20
    }
    return render(request, 'group/aboutUs.html',context)