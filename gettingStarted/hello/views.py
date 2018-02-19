from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):


    my_dict = {'insert_me':"Hellow this is rupesh !"}
    return render(request, 'hello/index.html', context = my_dict)
