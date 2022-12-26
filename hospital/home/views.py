from django.shortcuts import render
# from django.http import HttpResponse
from .models import Departments, Doctors,Contact

from .forms import BookingFrom
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingFrom(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conformation.html')
    form = BookingFrom()
    dict_form={
        'form': form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

# def contact(request):
#     return render(request,'contact.html')

def contact(request):
    if request.method=="POST":
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
    return render(request,'contact.html')

def department(request):
    dict_dpt={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dpt )

def anaesthesiology(request):
    return render(request,'anaesthesiology.html') 

def arthroscopy(request):
    return render(request,'arthroscopy.html') 

def audiology(request):
    return render(request,'audiology.html') 

def cardiac(request):
    return render(request,'cardiacanesthesia.html') 

def cardio(request):
    return render(request,'cardiothoracic.html') 

def cardiology(request):
    return render(request,'cardiology.html') 

def childcare(request):
    return render(request,'childguidance.html') 

def criticalcare(request):
    return render(request,'criticalcare.html')  