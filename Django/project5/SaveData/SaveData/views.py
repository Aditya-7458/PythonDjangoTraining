from mymodel.models import Mymodel
from django.shortcuts import render
def saveInfo(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')

        en=Mymodel(name=name,email=email,phone=phone)
        en.save()

    return render(request,"form.html")


def GetData(request):
    allData=Mymodel.objects.all()

    data={
        "allData":allData
    }
    return render(request,"Outputform.html",data)
    