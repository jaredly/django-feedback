# Create your views here.

def feedbackpost(request, url):
    if not request.POST:
        return render_to_response('feedback/basic_form.html',{})

