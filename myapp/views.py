from django.shortcuts import redirect, render
from matplotlib.style import context

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
                        return redirect('home/')
        else:
                #get request creates a blank form and renders it in the template
                form=Student_RegisterForm()
                        
                return render(request, 'Student_Register.html', {'form': form})
        