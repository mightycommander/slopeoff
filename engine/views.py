from django.template import loader
from django.http import HttpResponse
from .models import ResortInfo, get_recommendations
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm

# Create your views here.


def index(request):
    allResorts = ResortInfo.objects.order_by('id')[:20]
    context = {
        'allResorts': allResorts,
    }
    page_title = 'An example form and graph'

    form = ContactForm(request.form)

    if request.method == 'GET':
        return render(request, 'engine/index.html', context)

    if request.method == 'POST':
        flash("You just submitted a form. Yay!")
        return render(request, 'engine/index.html', context)
        '''
        plot = create_dummy_plot(
            project_id=request.form['project_id'],
            plot_type=request.form['plot_type'],
            color=request.form['plot_color']
        )
        script, div = components(plot)

        return render_template(
            'core/example.html', title=page_title, nav_links=nav_links, form=form, bokeh_script=script, div=div
        )
    '''



def detail(request, ResortName):

    resort = get_object_or_404(ResortInfo, ResortName=ResortName)
    return render(request, 'engine/detail.html', {'resort': resort})
