from django.shortcuts import render,HttpResponse
from .Forms import RegisterForm
from .models import RegisterModel
# Create your views here.


def Home(request):
    return render(request,'Home.html')

def myForm(request):
    if request.method == "POST":
        data_form = RegisterForm(request.POST)
        if data_form.is_valid():
            name = data_form.cleaned_data['name']
            email = data_form.cleaned_data['email']
            age = data_form.cleaned_data['age']
            address = data_form.cleaned_data['address']
            mobile = data_form.cleaned_data['mobile']
            date = data_form.cleaned_data['date']
            RegisterModel(name=name,email=email,age=age,address=address,mobile=mobile,data=date).save()
            return HttpResponse('Data Saved !!')
    else:  
     data_form = RegisterForm()
    return render(request,'Form.html',{'data_form':data_form})
