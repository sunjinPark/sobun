from kitchens.facade import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader, Context, Template

import json


@csrf_exempt
def cook_controller(request):
    facade = kitchen_facade()

    if request.method == 'GET':
        cook_list = facade.get_all_cook_list()

        t = loader.get_template('kitchen.html')
        c = Context({'item_list': cook_list})

        return HttpResponse(t.render(c))


@csrf_exempt
def take_food(request):
    facade = kitchen_facade()

    if request.method == 'GET':
        facade.take_cook()
        return HttpResponseRedirect('../kitchens')


@csrf_exempt
def alarm_to(request):
    facade = kitchen_facade()

    if request.method == 'POST':
        num = request.POST['num']

        facade.cook_finished(num)
        return HttpResponseRedirect('../kitchens')