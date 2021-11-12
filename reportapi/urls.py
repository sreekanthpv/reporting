from django.urls import path
from reportapi import views

urlpatterns=[
    path('reporting/accounts/signup',views.RegistrationView.as_view()),
    path('reporting/accounts/signin',views.SignInView.as_view()),
    path("reporting/courses/add",views.CourseView.as_view()),
    path("reporting/courses/view", views.CourseView.as_view()),
    path("reporting/batches/add",views.BatchView.as_view()),
    path("reporting/batches/view", views.BatchView.as_view()),

]