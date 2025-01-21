from django.shortcuts import render ,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


def student_signup_views(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']

        if len(password)<6:
            messages.error(request,"password must we greater then 6 charactor")
            return redirect('student_signup')
        if User.objects.filter(email).exists():
            messages.error(request,"this email allready register")
            return redirect('student_signup')
        user=User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()
        messages.error(request,"Employer account created successfully! Please log in.")
        return redirect('student_login')
    return render(request,'student_signup')

def employer_signup_views(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']

        if len(password)<6:
            messages.error(request,"password must we greater then 6 charactor")
            return redirect('employer_signup')
        if User.objects.filter(email).exists():
            messages.error(request,"this email allready register")
            return redirect('employer_signup')
        user=User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()
        messages.error(request,"Employer account created successfully! Please log in.")
        return redirect('employer_login')
    return render(request,'employer_signup')


