from django.shortcuts import render, HttpResponse
from .models import Remain
# Create your views here.
def index(request):
    myins = Remain(name="Naman25", desc="Good guy2534")
    myins.save()
    return HttpResponse("Hello, World!")