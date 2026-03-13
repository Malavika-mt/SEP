from django.contrib import admin
from django.urls import include, path

from myapp import views

urlpatterns = [
     path('',views.home,name='home'),
    
    path('contact/',views.contact,name='contact'),
    
    path('department/',views.department,name='department'),

    path('Student_Register/', views.Student_Register, name='Student_Register'),
]
