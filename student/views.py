from django.shortcuts import render, HttpResponse,redirect
from .forms import StudForm,Sform
from .models import stud
from datetime import date
from django.core.mail import send_mail
import uuid
from django.contrib import messages

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
        stud_obj = stud.objects.create(user = p,auth_token = str(uuid.uuid4))
        stud_obj.save()
        
        send_mail(
            "Submission of form",
            "Hello,Please verify your account http://127.0.0.1:8000/verify/{token}",
            "guptagaurish1011@gmail.com",
            [p.email],
            fail_silently=False
        )
        return render(request,"ack.html",{"title":"Verify email"})
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

def verify(request , auth_token):
    try:
        profile_obj = stud.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return render(request, 'ack.html')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return render(request, 'ack.html')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')
