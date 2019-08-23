from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages,auth

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logins(request):
    if request.user.is_authenticated:
        messages.info(request, f"You are now logged in as {request.user} ")
        return redirect('home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        return render(request = request,
                        template_name = "login.html",
                        context={"form":form})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request,"you are logged out")
        return redirect('home')
    
def about(request):
    return render(request,'about.html')