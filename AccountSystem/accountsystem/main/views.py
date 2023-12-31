from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 

def home(request):
    return render(request,"home.html", {})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles })
    else: 
        messages.success(request,("You must to be logged"))
        return render(request, 'home.html')
       
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("You Have Been Logged !"))
            return redirect('home')
        else:
            messages.success(request,("There was an error logging in..."))
            return redirect('login')

    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request,("You Have been logged out"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("Registered !"))
            return redirect('home')
            

    return render(request, "register.html", {'form':form})
