from django.shortcuts import render, HttpResponse, render_to_response
from base.models import Contact

# Create your views here.

def home(request):
    query  = Contact.objects.all()
    return render(request, 'home.html', {'query': query})




def ajax_function(request):
    if request.is_ajax():
        message = Contact.objects.create(name="test", phone="0665502911")
        Contact.objects.order_by("-date")
    else:
        message = "Not ajax"
    return HttpResponse(message)