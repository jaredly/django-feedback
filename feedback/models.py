from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class Feedback(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('site'))
    url = models.CharField(max_length=255, verbose_name=_('url'))
    urlhash = models.TextField(verbose_name=_('urlhash'), default="", null=True, blank=True)
    useragent = models.TextField(verbose_name=_('useragent'), default="", null=True, blank=True)
    subject = models.CharField(max_length=255, blank=True, null=True,
            verbose_name=_('subject'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('email'))
    text = models.TextField(verbose_name=_('text'))
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u'{url}: {subject}'.format(url=self.url, subject=self.subject)
