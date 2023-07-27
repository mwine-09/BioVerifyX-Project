from django.shortcuts import render
from .forms import InvigilatorLoginForm
from .models import Invigilator
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.




def showHome(request):
    template = 'Invigilator/home.html'
    return render(request,template)



def showLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You have logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('invigilator-login')

    else:
        template = 'Invigilator/login.html'
        return render(request, template)


def logout (request):
    logout(request)
    return redirect('invigilator-login')

@login_required
def updateUser(request):
    return "Uopdate user from here"
@login_required
def showSettings(request):
    return render(request,'Invigilator/settings.html')