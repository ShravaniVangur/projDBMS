from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import police_station


def index(request):
    items = police_station.objects.all()
    context = {'items':items}
    return render(request,'app/index.html',context)
    #return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
