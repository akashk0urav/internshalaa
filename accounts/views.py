from django.shortcuts import render ,redirect ,HttpResponse
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
        if User.objects.filter(username=email).exists():
            messages.error(request,"this email allready register")
            return redirect('student_signup')
        user=User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()
        messages.success(request,"Student account created successfully! Please log in.")
        return redirect('student_login')
    return render(request,'student_signup.html')

def employer_signup_views(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']

        if len(password)<6:
            messages.error(request,"password must we greater then 6 charactor")
            return redirect('employer_signup')
        if User.objects.filter(username=email).exists():
            messages.error(request,"this email allready register")
            return redirect('employer_signup')
        user=User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()
        messages.success(request,"Employer account created successfully! Please log in.")
        return redirect('employer_login')
    return render(request,'employer_signup.html')


def student_login_views(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')  # Redirect to the student's dashboard
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('student_login')

    return render(request, 'student_login.html')

# Employer Login View
def employer_login_views(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('employer_dashboard')  # Redirect to the employer's dashboard
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('employer_login')

    return render(request, 'employer_login.html')

# Logout View (shared)
def user_logout(request):
    logout(request)
    return redirect('landing_dashboard')