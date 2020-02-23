from django.shortcuts import render ,redirect,reverse
from .models import UserUploads
from django.http import HttpResponse , HttpResponseRedirect
from .compo.DataCleaner import DataCleaner
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

context = {}


@login_required(login_url='/accounts/login/')
def welcome(request):
    context['username']=str(request.user).capitalize()
    if request.method =='POST':
        file_  = request.FILES['dataset']
        print("file:",file_)
        fs = FileSystemStorage()
        file_name=fs.save(str(request.user)+'/'+file_.name,file_)
        file_url=fs.url(file_name)
        context['file_name'] = file_name
        return  HttpResponseRedirect(reverse('phasetwo:page2'))

    return render(request,'phasetwo/welcome.html',context)


@login_required(login_url='/accounts/login/')
def page2(request):
    file_name = context['file_name']
    media = settings.MEDIA_ROOT
    path = os.path.join(media,file_name)
    context['dataset_location'] = path
    df=pd.read_csv(path)
    head=df.head(10)
    context['columns']= head.columns
    context['head_df'] = head
    if request.method == 'POST':
        list_of_input_ids = request.POST.getlist('inputs')
        context['not_required_headers'] = list_of_input_ids
        return redirect('phasetwo:page3')


    return render(request,'phasetwo/part2.html',context)


@login_required(login_url='/accounts/login/')
def page3(request):
    dc = DataCleaner(context['dataset_location'],context['not_required_headers'])
    dc.start()
    dc.remove_uneccessary_data()
    dc.remove_na()
    dc.remove_duplicates()
    dc.converting_data_types()
    cleaned_df = dc.return_dataframe()
    context['cleaned_dataframe'] = cleaned_df
    context['description']=cleaned_df.describe()
    return render(request,'phasetwo/page3.html',context)

    


@login_required(login_url='/accounts/login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("phaseone:home"))