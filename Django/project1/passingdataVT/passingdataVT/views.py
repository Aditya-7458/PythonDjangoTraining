from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
def homepage(request):
   
    data={

        'title':'Homepage',
        'data':'Passing data from view to template',

        'list': ['adi','hello','rahul','fatima'],

       
        
    }
   
    return render(request,"index.html",data)

def home(request):
    return render (request,"index.html")

def info(request):
    data={
        'sd':[{'name':'Aditya','no':213534444,'add':'ITI'},
              
              {'name':'Adya','no':'992109706','add':'ITI'},
              {'name':'Atya','no':'123399706','add':'ITI'}
              
              ]
    }
    return render (request,"nameAndContacts.html",data)