from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.forms import modelformset_factory
from .forms import *

def index(request):
    username_pk = request.user.pk
    if username_pk is None:
        return redirect('login')
    else:
        student = None
        #student = StudentProfile.objects.get(username=request.user)
    context = {'student':student}
    return render(request, 'detention/index.html', context)

def studentregister(request):
    if request.method == "POST":
        form_register = StudentRegistrationForm(request.POST)
        if form_register.is_valid():
            register = form_register.save(commit=False)
            password = register.password
            user_username = register.username
            email = register.email
            user = User.objects.create_user(user_username, email, password)
            register.save()
            user.save()
            user = authenticate(username=user_username, password=password)
            login(request, user)
            return redirect('index')
    else:
        error = None
        form_register = StudentRegistrationForm()
    context = {'form_register':form_register,}
    return render(request, 'registration/student_registration_form.html', context)

def parentregister(request):
    if request.method == "POST":
        form_register = ParentRegistrationForm(request.POST)
        if form_register.is_valid():
            register = form_register.save(commit=False)
            password = register.password
            user_username = register.username
            email = register.email
            user = User.objects.create_user(user_username, email, password)
            register.save()
            user.save()
            user = authenticate(username=user_username, password=password)
            login(request, user)
            return redirect('index')
    else:
        error = None
        form_register = ParentRegistrationForm()
    context = {'form_register':form_register,}
    return render(request, 'registration/parent_registration_form.html', context)

