from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def add(request):
    return HttpResponse("group called...")

#Create views of Contact us page
def contactUs(request):
    return render(request, 'group/contactUs.html')

#Create views of index  page
def index(request):
    return render(request, 'group/index.html')

#Create views of Contact us page
def aboutUs(request):
    return render(request, 'group/aboutUs.html')