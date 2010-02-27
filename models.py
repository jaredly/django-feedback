from django.db import models
from django.contrib.sites.models import Site

class Feedback(models.Model):
    site = models.ForeignKey(Site)
    url = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField()

    def __unicode__(self):
        return u'%s: %s' % (self.url, self.subject)


# Create your models here.
