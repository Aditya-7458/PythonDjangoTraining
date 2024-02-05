from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("Welcome to firstproject URL")

def course(request):
    return HttpResponse("Welcome to our Course URL")

def courseDetails(request,courseid):
    return HttpResponse(courseid)


def homepage(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")


