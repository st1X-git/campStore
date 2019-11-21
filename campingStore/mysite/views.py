from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination
from .models import Staff


def index(request):
    # dest1 = Destination()
    # dest1.name = 'Abay'

    dests = Destination.objects.all()
    return render(request, "mysite/index.html", {'dests' : dests}) # return text in page
    ### We create templates dynamic for convience and working with html

def _Staff(request):
    person = Staff.object.all()
    return render(request, 'mysite/index.html', {'person' : persons })
