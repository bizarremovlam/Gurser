from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Salam Bu yer Products PAges")