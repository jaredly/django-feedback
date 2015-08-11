#!/usr/bin/env python
from django import forms
from django.contrib.sites.models import Site

from feedback.models import Feedback

class FeedbackForm(forms.ModelForm):
    '''The form shown when giving feedback'''
    class Meta:
        model = Feedback
        fields = "__all__"
        #exclude = ('site', 'url')

# vim: et sw=4 sts=4
