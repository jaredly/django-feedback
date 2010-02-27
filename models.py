from django.db import models

class Feedback(models.Model):
    site = models.ForeignKey(Site)
    url = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.url, self.subject)


# Create your models here.
