from django.template import loader
from django.http import HttpResponse
from .models import ResortInfo, get_recommendations
from django.shortcuts import render, get_object_or_404
from .forms import FilesForm
import numpy as np
from django.db.models import Case, When

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


    if request.method == "POST":
        form = FilesForm(request.POST)
        if form.is_valid():

            list_of_preferences = [form.cleaned_data['Continent'],form.cleaned_data['Level'],form.cleaned_data['Size'], form.cleaned_data['Price']]

            indic = get_recommendations(list(ResortInfo.objects.all().values()), list_of_preferences)
            id_list = list(indic)

            clauses = ' '.join(['WHEN "ResortName" = \'%s\' THEN %s' % (pk, i) \
                        for i, pk in enumerate(id_list)])

            ordering = 'CASE %s END' % clauses

            allResorts = ResortInfo.objects.filter(ResortName__in=id_list).extra(
                        select={'ordering': ordering}, order_by=('ordering',))


            return render(request, 'engine/index.html', {'form': form, 'allResorts': allResorts})

    elif request.method == "GET":
        form = FilesForm()
        return render(request, 'engine/index.html', {'form': form})



def detail(request, ResortName):

    resort = get_object_or_404(ResortInfo, ResortName=ResortName)
    return render(request, 'engine/detail.html', {'resort': resort})
