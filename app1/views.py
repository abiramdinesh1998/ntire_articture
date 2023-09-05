from django.shortcuts import render

# Create your views here.
from app1.models import *
from django.http import HttpResponse

def insert_webpage(request):
    LTO=topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=topic.objects.get(topic_name=tn)
        WO=webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        QSWO=webpage.objects.all()
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)   
    return render(request,'insert_webpage.html',d)