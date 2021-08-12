from django.shortcuts import render
from django.http import *

# Create your views here.

def reg(request):

    return render(request, "base.html")