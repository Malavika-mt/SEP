from django.contrib import admin
from django.urls import include, path

from myapp import views

urlpatterns = [
     path('',views.home,name='home'),
    
    path('contact/',views.contact,name='contact'),
    
    path('department/',views.department,name='department'),

    path('Student_Register/', views.Student_Register, name='Student_Register'),

    path('register/', views.register_user, name='register'),

    path('register_user/', views.register_user, name='register_user'),

    path('login/', views.login_user, name='login'),

    path('userhome/', views.user_home, name='userhome'),

    path('profile/',views.profile,name='profile'),

    path('logout/',views.logout_user,name='logout'),


]
