# Create your views here.
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.utils.encoding import force_unicode

import json
import forms

def sanitize(errors):
    dct = dict((str(k),list(force_unicode(a) for a in v)) for k,v in errors.items())
    return dct

def handle_ajax(request, url):
    if not request.POST:
        return HttpResponse(json.dumps({'error':'no post recieved'}))
    else:
        post = {}
        for k in request.POST:
            post[k] = request.POST[k]
        post['url'] = url
        post['site'] = Site.objects.get_current().id
        form = forms.FeedbackForm(post)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({}))
        else:
            
            return HttpResponse(json.dumps({'errors':sanitize(form.errors)}))


