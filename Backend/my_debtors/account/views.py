from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.forms import *


# Create your views here.
from .models import *
from .forms import *


def registerPage(request):
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('school_name')
            messages.success(request, 'Account as been successfully created for ' +  user )

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):


    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email = email, password = password )

        if user is not None:
            login(request, user)
            return redirect('schoolprofile')
        else:
            messages.info(request, 'Kindly confirm your email and password')
            
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def schoolProfile(request):

    context = {}
    return render(request, 'accounts/school_profile.html', context)

def guardianProfile(request):

    context = {}
    return render(request, 'accounts/guardian_profile.html', context)















