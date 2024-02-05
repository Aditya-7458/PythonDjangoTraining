from django.shortcuts import render

# Create your views here.

from mymodel.models import Mymodel

def homepage(request):
    modelData=Mymodel.objects.all()


    data={

        'd':modelData
    }

    return render (request,"index.html",data)