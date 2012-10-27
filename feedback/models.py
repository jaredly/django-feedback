from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _


class Feedback(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('site'))
    url = models.CharField(max_length=255, verbose_name=_('url'))
    subject = models.CharField(max_length=255, blank=True, null=True,
            verbose_name=_('subject'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('email'))
    text = models.TextField(verbose_name=_('text'))

    def __unicode__(self):
        return u'{url}: {subject}'.format(url=self.url, subject=self.subject)
