from display_board import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader, Context, Template


@csrf_exempt
def display(request):
    if request.method == 'GET':
        display = display_board()
        waiting_list = display.get_all_waiters()

        t = loader.get_template('display.html')
        c = Context({'item_list': waiting_list})

        return HttpResponse(t.render(c))