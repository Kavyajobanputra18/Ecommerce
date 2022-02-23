from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Employee
# Create your views here.
def addEmployee(request):
    emp = Employee(ename='john', eage=25 ,eemail= 'john@123', econtact=987654321)
    emp.save()
    return HttpResponse('Employee Added...')

def viewEmployee(request):
    employees = Employee.objects.all().values_list()
    print(employees)
    return render(request,'employee/view.html',{'employees':employees})

def deleteEmployee(request):
    emp = Employee.objects.get(id =1)
    emp.delete()
    return HttpResponse('Employee Deleted...')

def updateEmployee(request):
    emp = Employee.objects.get(id =2)
    emp.eage = 30
    emp.econtact = 1234567890
    emp.save()
    return HttpResponse('Employee updated...')