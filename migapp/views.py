from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from migapp.models import GreatObject

# Create your views here.

def easiest(request):
    gos = GreatObject.objects.all()
    data = {'objects': gos, }
    template = loader.get_template('easy.html')
    return HttpResponse(template.render(data))
