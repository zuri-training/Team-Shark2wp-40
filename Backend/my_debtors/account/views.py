from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
# from django.forms import *


# Create your views here.
from .models import *
from .forms import *
from account import views
from school.models import *

from django.views.generic import (
    ListView,
    DeleteView,
    DetailView
    )



@unauthenticated_user
def registerPage(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('school_name')
            messages.success(request, 'Your Account has been successfully been created')

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
   

@unauthenticated_user
def loginPage(request):
  
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
            
        user = authenticate(request, email = email, password = password )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Kindly confirm your email and password')
                
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')




class ListDebtor(ListView):
    template_name = 'school/dashboard.html'
    queryset = Debtor.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Debtor, id=id_)
    def get_success_url(self):
        return reverse('school:dashboard')

def guardianProfile(request):

    context = {}
    return render(request, 'accounts/guardian_profile.html', context)
















