from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request,'basicapp/index.html')
    return HttpResponse("Hello world, you are at the polls index.")

def form_name_view(request):
    form= forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)


        if form.is_valid():
            print('VALIDATION SUCCESS!')
            print("NAME:"+form.cleaned_data['name'])
            print("EMAIL:"+form.cleaned_data['email'])
            print("TEXT:"+form.cleaned_data['text'])



    return render(request,'basicapp/form_page.html',{'form':form})


    