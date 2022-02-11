from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addProduct(request):
    print("addproduct called....")
    return HttpResponse("addProduct called...")

#Create view product function to display the product page
def viewproduct(request):
    return HttpResponse("viewProduct called...")

#Create view product function to display the product page
def productpage(request):
    return render(request, 'product/productpage.html')
    
    


#Create view product function to display the aboutus page
def aboutus(request):
    return render(request,'product/aboutus.html')

#Create view product function to display the aboutus page
def contactus(request):
    return render(request,'product/contactus.html')

#Create view product function to display the aboutus page
def help(request):
    return render(request,'product/help.html')

