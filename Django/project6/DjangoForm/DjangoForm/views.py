from .form import MyForm
from django.shortcuts import render,redirect

def FormData(request):
    ans=0
    fn=MyForm()
    data={
        'form':fn
    }

    if request.method =="POST":
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        ans=n1+n2

        data={

            'form':fn,
            'n1':n1,
            'n2':n2
        }

       
    return render(request, "output.html",data)
    