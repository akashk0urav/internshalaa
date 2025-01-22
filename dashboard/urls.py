from django.urls import path
from . import views

urlpatterns = [
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('employer_dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('landing_dashboard/',views.landing_dashboard_views,name='landing_dashboard'),
]
