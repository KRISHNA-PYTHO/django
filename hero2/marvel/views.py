

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ironman(request):
    return HttpResponse('i m ironman')

def spiderman(request):
    return HttpResponse('i m spiderman')