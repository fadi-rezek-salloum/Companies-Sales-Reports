from email import message

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from profiles.forms import RegisterForm, LoginForm

def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                user = User.objects.create(username=username)
                user.is_active = True
                user.set_password(password)
                user.save()

                return HttpResponseRedirect('/login/')

            except:
                messages.error(request, 'Username already exists!')
                return HttpResponseRedirect('/register/')

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    form = LoginForm()

    if request.method=='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('sales:home')
            else:
                messages.error(request, 'Username or passwords are incorrect!')
                return HttpResponseRedirect('/login/')

    context = {
        'form': form,
    }

    return render(request, 'auth/login.html', context)