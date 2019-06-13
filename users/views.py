from django.shortcuts import render, redirect
from users.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request, 'users/register.html',
                      {'register_form': register_form})
    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            if request.POST.get('password1') != request.POST.get('password2'):
                return render(request, 'users/register.html',
                              {'register_form': register_form,
                               'errors': "Password and Confirm Password must be same."})
            user_obj = register_form.save(commit=False)
            user_obj.set_password(request.POST.get('password1'))
            user_obj.save()
            messages.add_message(
                request, messages.SUCCESS, "Registered Successfully.")
            return redirect('users:register')
        else:
            return render(request, 'users/register.html',
                          {'register_form': register_form})
    return redirect('users:login')


def login_user(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'users/login.html',
                      {'login_form': login_form})
    elif request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            user = authenticate(
                username=request.POST.get('username'),
                password=request.POST.get('password')
            )
            if user:
                login(request, user)
                return redirect('exam:home')
            else:
                return render(request, 'users/login.html',
                              {'login_form': login_form})
    return redirect('users:login')


@login_required
def logout_user(request):
    if request.method == 'GET':
        logout(request)
        return redirect('users:login')
    return redirect('/')
