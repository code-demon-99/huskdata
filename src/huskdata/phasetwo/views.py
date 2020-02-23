from django.shortcuts import render ,redirect,reverse
from .models import UserUploads
from .compo import DataCleaner
from django.core.files.storage import FileSystemStorage

def welcome(request):
    if request.method =='POST':
        file_  = request.FILES['dataset']
        print("file:",file_)
        fs = FileSystemStorage()
        file_name=fs.save(request.user.id+file_.name,file_)
        file_url=fs.url(fs.file_name)
        redirect('phasetwo:page2',file_url = file_url)
               
    return render(request,'phasetwo/welcome.html')

def page2(request, *args, **kwargs):
    pass