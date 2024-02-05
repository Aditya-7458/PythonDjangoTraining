from django.shortcuts import render,HttpResponse,HttpResponseRedirect



def calpost(request):
    ans=0
    try:
        if request.method =='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            ans=n1+n2
    except:
        pass
    return render (request,'post.html',{'ans':ans})

def cal(request):
    ans=0
    try:
        if request.method =='GET':
            n1=int(request.GET.get('num1'))
            n2=int(request.GET.get('num2'))
            ans=n1+n2
    except:
        pass
    return render(request,'form.html',{'ans':ans})

def submitform(request):
    return HttpResponse(request)
