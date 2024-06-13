from django.shortcuts import render
from .Forms import StudentForm

# Create your views here.


def index(request):
    return render(request,'index.html')

def register(request):
    form = StudentForm()
    return render(request,'Form.html',{'form':form})