from django.shortcuts import render,HttpResponse


def myfirstprogram(request):
    return HttpResponse("My First Program")

def add(request,a,b):
    return HttpResponse(f"addition : {a+b}")

def minus(request,a,b):
    return HttpResponse(f"minus : {a-b}")


def name(request,n):
    return HttpResponse(f"My name is {n}")



def prime_notprime(request,n):
    
    flag = 0
    for i in range(2,n):
        
        if(n%i==0):
            flag = 1
    
    if(flag == 0):
        return HttpResponse("It is prime number")
    else:
        return HttpResponse("It is not prime number")
    
    

def even_odd(request,n):
    
    if n%2 == 0:
        
        return HttpResponse("This is even number")
    
    else:
        
        return HttpResponse("This is odd number")
    
    
def index(request):
    return render(request,'index.html')


def Home(request,n):
    if n%2 == 0:
        return render(request,'Home.html',{'msg':'this is even no'})
    else:
        return render(request,'Home.html',{'msg':'this is odd number'})






