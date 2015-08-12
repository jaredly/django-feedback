from django.views.generic import CreateView
from django.conf import settings
from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

import json

from feedback.forms import FeedbackForm



class FeedbackView(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'

    def get_form_kwargs(self):
        kwargs = super(FeedbackView, self).get_form_kwargs()
        post = kwargs['data'].copy()
        post['url'] = self.kwargs['url']
        post['site'] = Site.objects.get_current().pk
        kwargs['data'] = post
        return kwargs

    def get_success_url(self):
        return self.kwargs['url']

    def form_valid(self, form):
        response = super(FeedbackView, self).form_valid(form)
        if hasattr(settings, 'FEEDBACK_EMAIL'):
            d = form.cleaned_data
            try:
                send_mail(
                        'Feedback received: {}'.format(d['subject']),
                        'email: {} \n\n {}'.format(d['email'], d['text']),
                        settings.SERVER_EMAIL,
                        [settings.FEEDBACK_EMAIL],
                        fail_silently=False,
                        )
            except:
                return HttpResponse(json.dumps({'error': _('Failed to send email')}))
        return HttpResponse(json.dumps({}))

    def form_invalid(self, form):
        return HttpResponse(json.dumps({'errors': form.errors}))

