from stores import store_facade
from menus import menu
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader, Context, Template

import json


@csrf_exempt
def login(request):
    if request.method == 'GET':
        t = loader.get_template('login.html')
        c = Context()
        return HttpResponse(t.render(c))


@csrf_exempt
def client_menu_list(request):
    facade = menu.menu_list()
    if request.method == 'GET':
        menu_list = facade.get_all_menu()

        t = loader.get_template('client_menu_list.html')
        c = Context({'item_list': menu_list})

        return HttpResponse(t.render(c))


@csrf_exempt
def order_info(request):
    facade = store_facade.store_facade()

    if request.method == 'POST':
        name = request.POST['name']
        menu_type = request.POST['type']
        facade.order_menu(menu_type, name)
        menu_list = facade.get_all_menu()

        print menu_list
        t = loader.get_template('order_list.html')
        c = Context({'item_list': menu_list})

        return HttpResponse(t.render(c))

    if request.method == 'GET':
        menu_list = facade.get_all_menu()
        t = loader.get_template('order_list.html')
        c = Context({'item_list': menu_list})

        return HttpResponse(t.render(c))
