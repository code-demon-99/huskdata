from django.contrib.auth import login, authenticate
from . import forms
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect, HttpResponse
#########################################################################################################################
def signup(request):

    form = forms.CustomUserCreationForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.username = form.cleaned_data.get('username')
            form.password = form.cleaned_data.get('password1')
            form.name=form.cleaned_data.get('name')
            form.email=form.cleaned_data.get('Email')
            form.save()
            return redirect('login:login')
    else:
        form = forms.CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})