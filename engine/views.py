from django.template import loader
from django.http import HttpResponse
from .models import ResortInfo, get_recommendations
from django.shortcuts import render, get_object_or_404
from .forms import FilesForm

# Create your views here.
nav_links = [
    {
        'link_text': 'HOME',
        'destination': 'core.index'
    },
    {
        'link_text': 'TEST EXAMPLE',
        'destination': 'core.example'
    },
    {
        'link_text': 'ANOTHER EXAMPLE',
        'destination': 'core.another_example'
    },
    {
        'link_text': 'MVT GUIDE',
        'destination': 'core.guide'
    }
]

def index(request):
    allResorts = ResortInfo.objects.order_by('id')[:20]
    context = {
        'allResorts': allResorts,
    }
    page_title = 'An example form and graph'
    form = FilesForm()


    return render(request, 'engine/index.html', {'form': form, 'allResorts': allResorts})





def detail(request, ResortName):

    resort = get_object_or_404(ResortInfo, ResortName=ResortName)
    return render(request, 'engine/detail.html', {'resort': resort})
