from django.template import loader
from django.http import HttpResponse
from .models import ResortInfo, get_recommendations
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    allResorts = ResortInfo.objects.order_by('id')[:20]
    context = {
        'allResorts': allResorts,
    }
    return render(request, 'engine/index.html', context)



def detail(request, ResortName):

    resort = get_object_or_404(ResortInfo, ResortName=ResortName)
    return render(request, 'engine/detail.html', {'resort': resort})
