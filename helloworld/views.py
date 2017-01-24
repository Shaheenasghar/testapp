from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import BSIT
from django.http import HttpResponse
# Create your views here.
def index(request):
    all_semesters= BSIT.objects.all() #all entries in bsit table
    template= loader.get_template('helloworld/index.html') #loading the html template for separating backend concept from view
   #dictionary it has info that template needs
    context={'all_semesters':all_semesters,}
    return HttpResponse(template.render(context, request))#passing the all info into the template

def details(request, BSIT_id):
    try:
        bsit=BSIT.objects.get(pk=BSIT_id)
    except BSIT.DoesNotExist:
        raise Http404("Class Does not exist")
    template= loader.get_template('helloworld/details.html')
    context2=  {'bsit':bsit,}  
    return HttpResponse(template.render(context2, request))
