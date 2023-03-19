from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterUser, LoginUser
from django.contrib import messages

# Create your views here.

def profile_view(request):
    user = request.user
    return render(request,"profile.html", {"user":user})

def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(request, 'register.html', {"form": form})
    else:
        form = RegisterUser()
        return render(request, 'register.html', {"form": form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            form = LoginUser()
            return render(request, 'login.html', {"form": form}) 
    else:
        form = LoginUser()
        return render(request, 'login.html', {"form": form})

def logout_user(request):
    logout(request)
    return redirect('/login')