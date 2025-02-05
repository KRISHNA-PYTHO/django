from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def batman(request):
    return HttpResponse('i m batman')

def superman(request):
    return HttpResponse('i m superman')