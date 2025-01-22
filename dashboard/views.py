from django.shortcuts import render

# Create your views here.
def student_dashboard(request):
    return render(request, 'student_dashboard.html')


def employer_dashboard(request):
    return render(request, 'employer_dashboard.html')


def landing_dashboard_views(request):
    return render(request, 'landing_dashboard.html')