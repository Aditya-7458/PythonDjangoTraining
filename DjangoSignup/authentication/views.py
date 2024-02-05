from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    return render(request,"authentication/index.html")


def signin(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"authentication/index.html",{'fname':fname})
        
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')

    return render (request,"authentication/signin.html")



def signup(request):
       
    if request.method=="POST":
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('confirmPassword')
        
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname

        myuser.save()
        messages.success(request,"Your Account has been created")
        return redirect('signin')

    return render (request,"authentication/signup.html")




def signout(request):
     return HttpResponse("Bye Bye")





