Feedback
========

creates an ajax "feedback" button on your site, which pops up a form for the
user to fill.

Usage (only requires template modifications)::

    <!-- in header block -->
    {% include "feedback/header.html" %}
    
    <!-- in body block -->
    {% include "feedback/button.html" %}

You also need to symlink feedback/media into your static media directory.
