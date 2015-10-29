from django.contrib import admin
from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ( 'site', 'url', 'urlhash', 'useragent', 'subject', 'email', 'text', 'created' )


admin.site.register(Feedback, FeedbackAdmin)

# vim: et sw=4 sts=4
