from django.shortcuts import render
from .forms import InvigilatorLoginForm
from .models import Invigilator
from django.contrib.auth import authenticate, login
from .forms import InvigilatorLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.




def showInvigilatorIndex(request):
    return render(request,'Invigilator/index.html')


def showLogin(request):
    if request.method == 'POST':
        form = InvigilatorLoginForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username == username,password == password)
            if user is not None:
                login(request,user)

                return redirect('Invigilator/home.html')

            else:
                # Handle invalid credentials
                form.add_error(None, 'Invalid username or password.')
   
    else:
        form = InvigilatorLoginForm()
    return render(request,'Invigilator/login.html', {'form': form})




def logout(request):
    return "You have logged out successfully"



@login_required
def updateUser(request):
    return "Uopdate user from here"
@login_required
def showSettings(request):
    return render(request,'Invigilator/settings.html')