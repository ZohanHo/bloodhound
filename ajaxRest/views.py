from django.shortcuts import render, HttpResponse, render_to_response
from base.models import Contact
import json



def renderList(request):
    return render(request, 'ajaxRest.html', context={})

def change(request):

    return render(request, 'ajaxrestpost.html', context={})