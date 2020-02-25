from django.shortcuts import render,redirect
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('phasetwo:welcome'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    return render(request, 'huskdata/Log-in.html')
###########################################################################

###########################################################################
def signup(request):
    """ User Register View"""
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
        except:
            return HttpResponse("please enter valid username/password")
        # finally saving the form
        user.save()
        return redirect('phaseone:login')
    else:
        # main register paghe load on first call
        return render(request, 'huskdata/signup.html',)
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
