from django.shortcuts import render, HttpResponse, render_to_response
from base.models import Contact
from django.http import JsonResponse
from django.db.models import Q
import json

def search(request):
    data = {}
    result_list = []
    value_input = request.GET.get('value_input', None)

    if value_input:
        result_list = [(user.name, user.phone) for user in Contact.objects.filter(
            Q(name__icontains=value_input) | Q(phone__icontains=value_input))]
        data = {
            "result": result_list,
            "value_input": value_input,
        }
        # возвращает строку, представляющую объект json из объекта
    return HttpResponse(json.dumps(data))

def home(request):
    query = Contact.objects.order_by("-date")

    # if request.method == "GET":
    #     search_text = request.GET.get('search')
    #     if search_text is not None and search_text != u"":
    #         search_text = request.GET['search']
    #         statuss = Contact.objects.filter(name__contains=search_text)
    #     else:
    #         statuss = []
    #
    #     #employees = Contact.objects.filter(Q(employee_position_q__icontains=search_text))
    #     #employees = employees | Contact.objects.filter(Q(name__icontains=search_text))
    #     #employees = employees | Contact.objects.filter(Q(salary_amount__icontains=search_text))
    #     #employees = employees | Contact.objects.filter(Q(date__icontains=search_text))
    #     return render(request, 'home.html', {"status": statuss})
    return render(request, 'home.html', {'query': query})

# def search(request):
#     if request.is_ajax():
#         #RequestGet = request.GET
#
#         # search_text = RequestGet.get("search")
#         # employees = Contact.objects.filter(name__icontains=search_text)
#         # search_dict = {}
#         # for key in employees:
#         #     search_dict[key.name] = key.name
#         # print(search_dict)
#         response = {"key" : "vaalue"}
#     else:
#         response = "Not ajax"
#     return JsonResponse(response)


def ajax_function(request):
    if request.is_ajax():
        #Contact.objects.create(name="test1", phone="0665502911")
        query = Contact.objects.order_by("name")
        #query = Contact.objects.all()
        #распарсиил кверисет, добавил имя в словарь
        dictro = {}
        for key  in query:
            dictro[key.name] = key.name

        response = dictro
    else:
        response = "Not ajax"
    return JsonResponse(response)