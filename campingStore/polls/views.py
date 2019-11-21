from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html') # return text in page
    ### We create templates dynamic for convience and working with html
