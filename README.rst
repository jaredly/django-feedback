Feedback
========

    As you might notice from the `last edit date` on most of these files, I haven't been using Django for a while now. As such, this project is **open for adoption**, and while I'm happy to still accept pull requests, I don't expect to develop new changes.



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

+ All feedback can be seen in the Django admin interface

+ Feedback can optionally be emailed to you as well, as it is submitted. Specify your email address in settings.py:

    FEEDBACK_EMAIL = "me@example.com"
