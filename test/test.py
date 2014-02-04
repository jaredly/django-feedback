#!/usr/bin/env python

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'

from django.test.utils import setup_test_environment

setup_test_environment()

import feedback.urls
import feedback.forms
import feedback.models
import feedback.admin
import feedback.views


# vim: et sw=4 sts=4
