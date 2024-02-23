from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators  import login_required
from .forms import UserProfileForm


from .models import *
from .forms import CreateUserForm


def landing(request):
  return render(request,'landing.html')

def loginpage(request):
  if request.method =='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('services')
    else:
      messages.info(request, 'Username or Password Incorrect')
  context={}
  return render(request, 'loginpage.html',context)

def registerpage(request):
  
  form=CreateUserForm()
  if request.method =='POST':
    form=CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user=form.cleaned_data.get('username')
      messages.success(request, 'Registered Succesfully!')
      return redirect('login')
  context ={'form':form}
  return render(request, 'register.html', context)

def logoutpage(request):
  logout(request)
  return redirect('landing')


def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = UserProfileForm()

    return render(request, 'user_profile.html', {'form': form})


#login_required(login_url='login')
def services(request):
  return render(request,'services.html')


#----------base services----------
#login_required(login_url='login')
def med_ser(request):
  return render(request,'med_ser.html')
#login_required(login_url='login')
def wellness(request):
  return render(request,'wellness.html')
#login_required(login_url='login')
def vaccination_base(request):
  return render(request,'vac_base.html')
#login_required(login_url='login')
def diet_cons1(request):
  return render(request,'diet_cons1.html')
#login_required(login_url='login')
def diet_cons2(request):
  return render(request,'diet_cons2.html')

def home(request):
  return render(request,'home.html')

def vac_base_archive(request):
  return render(request,'vac_base_archive.html')