from django.shortcuts import render
from .forms import FormPopup
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Contact


def PopupView(request):
    if request.method == 'POST':
        form = FormPopup(request.POST)
        if form.is_valid():
            name  = form.cleaned_data.get("name")
            phone = form.cleaned_data.get("phone")
            Contact.objects.create(name=name, phone=phone)
            return HttpResponseRedirect('/submit/')
    else:
        form = FormPopup()
    return render(request, "base/home.html", context={'form': form})



def Submit(request):
    return render(request, "base/submit.html", context={})


def Get_absolute_url_list(request):
    Query_Contact = Contact.objects.all()
    return render(request, "base/get_abs_url_list.html", context={"Query_Contact": Query_Contact})

def Get_absolute_url_detail(request, pk):
    obj = Contact.objects.get(pk=pk)
    return render(request, "base/get_absolute_url_detail.html", context={"obj": obj})