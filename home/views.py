from django.shortcuts import render
from home.models import Settings

from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    settings = Settings.objects.get(pk=1)
    context={"settings":settings}    
    return render(request,'index.html',context)