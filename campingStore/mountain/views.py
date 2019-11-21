from django.http import HttpResponse
from django.shortcuts import render
# from .models import Destination


def index(request):
    dests = Destination.objects.all()
    return render(request, 'mountain/index.html') # return text in page
    ### We create templates dynamic for convience and working with html
