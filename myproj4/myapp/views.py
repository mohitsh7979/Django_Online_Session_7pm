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