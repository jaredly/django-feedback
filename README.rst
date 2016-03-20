Feedback
========

Creates an ajax "feedback" button on your site, which pops up a form for the
user to fill.

+ Add it to your installed apps::

    INSTALLED_APPS += ('feedback',)


+ Sync the database

+ Add a line to your urls.py::

    url(r'^feedback/', include('feedback.urls')),

+ Use it (only requires template modifications)::

    <!-- in header block -->
    {% include "feedback/header.html" %}
    
    <!-- in body block -->
    {% include "feedback/button.html" %}

+ Or use your own button which pops up feedback form::

    <!-- in body block -->
    {% include "feedback/feedback.html" %}
    <div class="feedback_button"/>
   

+ All feedback can be seen in the Django admin interface

+ Class "modal-open" is added to body for compatibility with Bootstrap modal.

+ Feedback can optionally be emailed to you as well, as it is submitted. Specify your email address in settings.py:

    FEEDBACK_EMAIL = "me@example.com"
