from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login

from myapp.models import Student_Register
from myapp.forms import Student_RegisterForm
from myapp.models import Department

# Create your views here.
def home(request):
        
        return render(request, 'base.html')

#request is an object that contains all the information
#about the request that was made to the server.

def contact(request):
        
        return render(request, 'contact.html')


def department(request):
        alldepartment=Department.objects.all()
        print(alldepartment)
        
        context={ 'departments':alldepartment,
                 'page_title':'department details',
                 'description': 'details...',
                }              
        
       

        return render(request,'department.html',context)


#post does not show the data in the url and get shows the data in the url
#seesion is a way to store data for a particular user across multiple requests
#unique Identification is a way to identify a user uniquely across multiple requests
        
def Student_Register(request):
        if request.method == 'POST':
                form= Student_RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('home')
                else:
                        return render(request, 'Student_Register.html', {'form': form})
        else:
                #get request creates a blank form and renders it in the template
                form=Student_RegisterForm()
                        
                return render(request, 'Student_Register.html', {'form': form})
        
def register_user(request):
        if request.method == 'POST':
                form= Student_RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('login')
                else:
                        return render(request, 'register.html', {'form': form})
        else:
                #get request creates a blank form and renders it in the template
                form=Student_RegisterForm()
                        
                return render(request, 'register.html', {'form': form})
        
def login_user(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        return redirect('userhome')
                else:
                        return render(request, 'login.html', {'error': 'Invalid credentials'})
        else:
                return render(request, 'login.html')

def logout_user(request):
        logout(request)
        return redirect('home/')

def user_home(request):
        return render(request, 'userhome.html')

def profile(request, id):
        profile = Student.objects.get(id=id)

        if request.user!= profile.user:
                return HttpResponseForbidden("You are not authorized to view this profile")
        return HttpResponse(f"Welcome to the profile page ")
        
