from django.shortcuts import render,redirect
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError



###################################################################
def home_view(request):
    """
        home view or say main page for the project
    """
    return render(request, "huskdata/home.html")
######################################################################

######################################################################
def login(request):
    """User Login View """
    msg=""
    if request.user.is_authenticated:
        return redirect('phasetwo:welcome')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('phasetwo:welcome'))
            else:
                msg = "Your account was inactive. please contact Project admin by contact us form on home page"
        else:
            msg = " cant login given usename/password is invalid!!!! "
    return render(request, 'huskdata/Log-in.html',context={'message':msg})

          

###########################################################################

###########################################################################
def signup(request):
    msg =""
    if request.user.is_authenticated:
        return redirect('phasetwo:welcome')

    if request.method == "POST":
        # user details collection
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # checking user can be saved or not
        try:
            user=User.objects.create_user(username=username, password=password,email=email,first_name=fname,last_name =lname)
        else:
            msg= "please create another username/password it cannot be created "
        # finally saving the form
            user.save()
            return redirect('phaseone:login')
        except IntegrityError as e: 
            msg = "please create another username/password it cannot be created(user already exists) "

        # main register paghe load on first call
    return render(request, 'huskdata/signup.html',context={'message':msg})
##############################################################################

##############################################################################

# about us  section
def aboutus(request):
    """main"""
    return render(request,'huskdata/aboutus.html');

#def portone(request):
  #  """ portfolio for rishi """
 #   return redirect('portfolio-rishi-namdev.atwebpages.com')


def porttwo(request):
    """ portfolio for sumit """
    return render(request,'huskdata/aboutsumit.html')

def portthree(request):
    """ portfolio for ritika """
    return render(request,'huskdata/aboutritika.html')

#################################################################################
