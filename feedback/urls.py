from django.conf.urls.defaults import patterns, url

from feedback.views import FeedbackView

urlpatterns = patterns('',
        url(r'^ajax(?P<url>.*)$', FeedbackView.as_view(), name='feedback'),
    )

# vim: et sw=4 sts=4
