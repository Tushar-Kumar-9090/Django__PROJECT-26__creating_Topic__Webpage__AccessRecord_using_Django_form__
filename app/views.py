from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
## Create your views here.

def display_topic(request):
    TO = TopicForm()
    d = {'TO':TO}
    
    if request.method == 'POST':
        TODT=TopicForm(request.POST)
        if TODT.is_valid():
            topic_name=TODT.cleaned_data['topic_name']
            TO1=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO1.save()

            return HttpResponse("<center><h1>Topic Data Submitted</h1></center>")
    return render(request,'insert_data/topic.html',d)


def display_webpage(request):
    WO = WebpageForm()
    d = {'WO':WO}
    
    if request.method == 'POST':
        WODT=WebpageForm(request.POST)
        if WODT.is_valid():
            topic_name=WODT.cleaned_data['topic_name']
            name=WODT.cleaned_data['name']
            url=WODT.cleaned_data['url']
            
            TO1=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO1.save()

            WO1=Webpage.objects.get_or_create(topic_name=TO1, name=name, url=url)[0]
            WO1.save()
            return HttpResponse("<center><h1>Webpage Data Submitted</h1></center>")
    return render(request,'insert_data/webpage.html',d)


def display_access_record(request):
    ACO = AccessRecordForm()
    d = {'ACO':ACO}
    
    if request.method == 'POST':
        ACODT=AccessRecordForm(request.POST)
        if ACODT.is_valid():
            name=ACODT.cleaned_data['name']
            date=ACODT.cleaned_data['date']
            author=ACODT.cleaned_data['author']
            
            WO1=Webpage.objects.get(name=name)
            WO1.save()

            ACO1=AccessRecord.objects.get_or_create(name=WO1, date=date, author=author)[0]
            ACO1.save()
            return HttpResponse("<center><h1>Access Record Data Submitted</h1></center>")
    return render(request,'insert_data/access.html',d)
