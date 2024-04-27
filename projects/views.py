from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators  import login_required
from .forms import UserProfileForm, EventsForm, CreateUserForm
from .models import Events, UserProfile


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
  form = UserProfileForm()
  print(request.method)  # Debugging
  if request.method == 'POST':
    print(request.POST)  # Debugging
    form = UserProfileForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('user_profile')
    else:
      form = UserProfileForm()
  return render(request, 'user_profile.html', {'form': form})





def view_profile(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    return render(request, 'view_profile.html', {'user_profile': user_profile})


     
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
    print(request.method)  # Debugging
    if request.method == 'POST':
        print(request.POST)  # Debugging
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vac_base')
    else:
        form = EventsForm()
    return render(request, 'vac_base.html', {'form': form})

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
def nearest_vet(request):
  return render(request,'nearest_vet.html')
def home_visit(request):
  return render(request,'home_visit.html')
def insurance(request):
  return render(request,'insurance.html')
def bmi_calc(request):
  return render(request,'bmi_calc.html')
def feedback(request):
  return render(request,'feedback.html')



def calender(request):
  events = Events.objects.all()  # Adjust this query as needed
  return render(request, 'calender.html', {'events': events})