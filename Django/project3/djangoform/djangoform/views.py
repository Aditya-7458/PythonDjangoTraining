from .form import userForm
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def showFormData(request):
    ans=0
    fn=userForm()
    data={
        'form':fn
    }

    try:
        if request.method=='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            ans=n1+n2
            data={
                 'form':fn,
                 'output':ans,
                 'n1':n1,
                 'n2':n2
            }

    except:
        pass
    return render(request,'index.html',data)

def thanks(request):
    return render(request,"thanks.html")

