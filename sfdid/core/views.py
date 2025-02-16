from django.shortcuts import render
from . forms import AdmissionForm
from . models import CollegeAdmission
# Create your views here.

def index(request):
    if request.method =='POST':
        mf = AdmissionForm(request.POST)
        if mf.is_valid():
            f_name = mf.cleaned_data['name']
            l_name = mf.cleaned_data['last_name']
            print(f_name)
            print(l_name)
            CollegeAdmission(name=f_name,last_name=l_name).save()
            mf=AdmissionForm()
    else:
        mf= AdmissionForm()
    return render(request,'core/index.html',{'mf':mf})