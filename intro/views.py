from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""def home(request):
    return HttpResponse("Hello")

def room(request):
    return HttpResponse("hy")"""


"""def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')"""


Details = [
    {'id':1,  'name':'Ravikanta!'},
    {'id':2,  'name':'Megha'},
    {'id':3,  'name':'Juhi'},
]

"""def home(request):
    context={'Details':Details}
    return render(request, 'home.html',context)

def room(request):
    return render(request, 'room.html')"""

def home(request):
    context={'Details':Details}
    return render(request, 'intro/home1.html',context)

#def room(request):
    #return render(request, 'intro/room1.html')

#def room(request, pk):
    #return render(request, 'intro/room1.html')

def room(request, pk):
    detail=None
    for i in Details:
        if i['id'] == int(pk):
            detail=i
    context={'detail': detail}   
    return render(request, 'intro/room1.html',context)