#!/usr/bin/env python

from django.test import TestCase
from django.core.urlresolvers import reverse

class ViewTestCase(TestCase):
    """Test project views."""

    def test_feedback_view(self):
        """A POST should log the error"""
        post_data = {
        "text": "sample test text",
        }
        response = self.client.post(reverse('feedback', kwargs={'url': 'test_url'}), post_data)
        self.assertEqual(response.content, b"{}")
        self.assertEqual(response.status_code, 200)

    def test_error_view(self):
        """A POST should log the error"""
        response = self.client.post(reverse('feedback', kwargs={'url': 'test_url'}))
        self.assertEqual(response.content, b'{"errors": {"text": ["This field is required."]}}')
        self.assertEqual(response.status_code, 200)

# vim: et sw=4 sts=4
