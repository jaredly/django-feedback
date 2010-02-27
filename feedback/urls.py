from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from views import handle_ajax

urlpatterns = patterns('',
        (r'^ajax(?P<url>.*)$', handle_ajax)
    )

# vim: et sw=4 sts=4
