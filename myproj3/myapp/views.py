from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'Home.html')

def about(request):
    return render(request,'About.html')

def blog(request):
    return render(request,'Blog.html')

def contact(request):
    return render(request,'Contact.html')
