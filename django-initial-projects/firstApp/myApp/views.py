from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from myApp.models import Topic, Question, Webpage, AccessRecord


# def index(request):
#     my_dict = {'inser_me': "hello how are you jayant"}
#     return render(request, 'firstApp/index.html', context=my_dict)

# def help(request):
#     helpdict={'help_insert':'HELP PAGE'}
#     return render(request,'firstApp/help.html',context=helpdict)


def indexOne(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    return render(request, 'firstApp/indexOne.html', context=date_dict)