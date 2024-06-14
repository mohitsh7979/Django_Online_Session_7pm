from django.shortcuts import render,HttpResponse
from .forms import StudentForm
from .models import Student

# Create your views here.

def index(request):
    if request.method == "POST":
        form_data = StudentForm(request.POST,request.FILES)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('data Saved !!')
    form_data = StudentForm()
    data = Student.objects.all()
    context = {
        'form_data':form_data,
        'data':data
    }
    return render(request,'index.html',context)
