from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'core/index.html')

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

def customer(request):
    return render(request,'core/customer.html')

def project(request):
    return render(request,'core/project.html')