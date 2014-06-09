from menus.facade import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader, Context, Template

import json


@csrf_exempt
def menu_control(request):
    facade = menu_facade()

    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        menu_type = request.POST['type']
        facade.create_menu(name, price, menu_type)
        menu_list = facade.get_all_menu()
        rendering_list = list()

        print menu_list
        t = loader.get_template('menu_list.html')
        c = Context({'item_list': menu_list})

        return HttpResponse(t.render(c))

    if request.method == 'GET':
        menu_list = facade.get_all_menu()

        t = loader.get_template('menu_list.html')
        c = Context({'item_list': menu_list})

        return HttpResponse(t.render(c))


@csrf_exempt
def delete_page(request):
    facade = menu_facade()
    if request.method == 'GET':
        t = loader.get_template('delete.html')
        c = Context()
        return HttpResponse(t.render(c))

    if request.method == 'POST':
        name = request.POST['name']
        if name == "all":
            facade.delete_all()
        facade.delete_menu(name)
        print "delete"
        menu_list = facade.get_all_menu()

        t = loader.get_template('menu_list.html')
        c = Context({'item_list': menu_list})

        return HttpResponseRedirect('../')


@csrf_exempt
def insert_page(request):
    if request.method == 'GET':
        t = loader.get_template('insert.html')
        c = Context()
        return HttpResponse(t.render(c))
