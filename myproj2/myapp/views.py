from django.shortcuts import render

# Create your views here.

def index(request,name):
    return render(request,'index.html',{'name':name})

def Home(request):
    return render(request,'Home.html')

def About(request):
    return render(request,'About.html')

def Product(request):
    return render(request,'Product.html')
