from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from django import forms


# Registers an account with a username, password, and email address
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = changePic(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Profile Picture has been updated!')
            return redirect('profile')
    
    else: 
        form = changePic(instance=request.user.profile)
        
    return render(request, 'users/profile.html', {'form': form})

class changePic(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



