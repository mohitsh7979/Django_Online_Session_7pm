from django.shortcuts import render,HttpResponse,redirect
from .models import Student
# Create your views here.

def index(request):
    data = Student.objects.all()
    return render(request,'Table.html',{'data':data})

def getForm(request):
    if request.method == "POST":
        name = request.POST['uname']
        email = request.POST['uemail']
        address = request.POST['address']
        mobile = request.POST['mobile']
        date = request.POST['date']
        age = request.POST['age']
        Student(name=name,email=email,age=age,address = address,mobile_no=mobile,date=date).save()
        return redirect('/')
    return render(request,'Form.html')

def deletehandle(request,id):
    data = Student.objects.filter(id=id)
    data.delete()
    return redirect('/')

def updatehandle(request,id):
    if request.method == "POST":
        data = Student.objects.get(id=id)
        data.name = request.POST['uname']
        data.email = request.POST['uemail']
        data.address = request.POST['address']
        data.mobile_no = request.POST['mobile']
        data.date = request.POST['date']
        data.age = request.POST['age']
        data.save()
        return redirect('/')
    else:
        data = Student.objects.get(id=id)
   
    return render(request,'Update.html',{'data':data})