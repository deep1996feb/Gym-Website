
from django.http.response import HttpResponse
from django.shortcuts import render
from django. http import HttpResponse
from gym. models import Customers
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
         name = request.POST.get('name')
         age = request.POST.get('age')
         mobile = request.POST.get('mobile')
         address = request.POST.get('address')
         customers = Customers(name = name, age = age, mobile = mobile, address = address)
         customers.save()
         messages.success(request, 'Your form has been submitted.')
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')