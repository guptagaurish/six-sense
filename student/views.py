from django.shortcuts import render, HttpResponse
from .forms import StudForm,Sform
from .models import stud
from datetime import date
from django.core.mail import send_mail

def existing(request):
    title="All Registered Students"
    queryset = stud.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request,'existing.html',context)




def register(request):
    title = "New Student Enrollment"
    form = StudForm(request.POST or None)
    
    if form.is_valid():
        #import datetime
        name = form.cleaned_data['name']
        contact = form.cleaned_data['contact']
        email = form.cleaned_data['email']
        dob = form.cleaned_data['dob']
        
        age = (date.today() - dob).days / 365
        if age < 18:
            return HttpResponse("Your age is less than 18, not allowed to fill the form")
            

        p = stud(name = name, contact = contact, email = email,dob = dob)

        p.save()
        
        send_mail(
            "Submission of form",
            "Hello,Thank you for registering with us ; Your Form is succesfully Submitted and you are registered.",
            "guptagaurish1011@gmail.com",
            [p.email],
            fail_silently=False
        )
        return render(request,"ack.html",{"title":"Registered Successfully"})
        #
        

    context = {
        "title":title,
        "form": form,

    }

    return render(request,"register.html",context)

def existing(request):
    title="All Registered Students"
    queryset = stud.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request,'existing.html',context)

def search(request):
    title="Search Student"
    form = Sform(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        queryset = stud.objects.filter(name=name)
        context={
            'title':title,
            'queryset':queryset,
        }
        return render(request, 'existing.html',context)
    context={
        'title':title,
        'form':form,
    }
    return render(request, "search.html",context)