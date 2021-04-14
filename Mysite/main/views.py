from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello yopta")
    return render(request, 'main/index.html')

