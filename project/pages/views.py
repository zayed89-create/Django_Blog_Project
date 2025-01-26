from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .forms import Loginform 
# Create your views here.
def index(request):
     x={'name':'zizo','age':254548454544415}
     return render(request,'pages/index.html',x)
def about(request):

    if request.method=='Post': 
       dataform=Loginform(request.POST)
       if dataform.is_valid:
           dataform.save()



   
    return render(request,'pages/about.html',{'lf':Loginform}) 