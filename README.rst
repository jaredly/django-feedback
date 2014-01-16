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
