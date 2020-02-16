from django.shortcuts import render

# Create your views here.
def aboutus(request):
    return render(request,'aboutus.html');

def portone(request):
    return render(request,'aboutrishi.html')

def porttwo(request):
    return render(request,'aboutsumit.html')

def portthree(request):
    return render(request,'Template/aboutritika.html')
