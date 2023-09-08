from django.shortcuts import render

# Create your views here.
from app.views import *
from app.models import *
from app.forms import *


def insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            Sname=SFD.cleaned_data['Sname']
            Sid=SFD.cleaned_data['Sid']
            Semail=SFD.cleaned_data['Semail']
            SO=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            SO.save()

    return render(request,'insert_student.html',d)
