from django.urls import path
from . import views

urlpatterns = [
    path('student_signup/', views.student_signup_views, name='student_signup'),
    path('employer_signup/', views.employer_signup_views, name='employer_signup'),
    path('student_login/', views.student_login_views, name='student_login'),
    path('employer_login/', views.employer_login_views, name='employer_login'),
    path('logout/', views.user_logout, name='logout'),


]
