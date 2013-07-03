#from firedeptmanagement.personal.models import Firefighter
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings

def frontpage(request):
    data = {}
    data['ga'] = settings.GA
    data['FF_SAMPLE_LOCATION'] = settings.FF_SAMPLE_LOCATION
    return render_to_response('frontpage.html', RequestContext(request, data))

def stats(request):
    data = {}
    data['ga'] = settings.GA
    data['STATS_LOCATION'] = settings.STATS_LOCATION
    return render_to_response('stats.html', RequestContext(request, data))


