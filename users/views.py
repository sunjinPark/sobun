from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context, Template
from django.views.decorators.csrf import csrf_exempt
from users.models import User
import json


def main(request):

    if "user_id" in request.session:
        sessionid = request.session["user_id"]
        t = loader.get_template('menu_list.html')
        c = Context({'user_id': sessionid},)
    else:
        t = loader.get_template('login.html')
        c = Context()

    return HttpResponse(t.render(c))


@csrf_exempt
def login(request):

    print '\n\nlogin'

    if request.method == 'POST':

        try:
            user_id = request.POST['user_id']
            pwd = request.POST['pwd']
            user = User.objects.get(user_id=user_id)
            if not pwd == user.pwd:
                msg = "Password Incorrect"
                status = 0
            else:
                request.session['user_id'] = user_id
                msg = "Login Success"
                status = 1
        except Exception as e:
            msg = str(e)
            status = 0
            print e

        dict = {'user_id': user_id, 'msg': msg, 'status': status}

        return HttpResponse(json.dumps(dict), mimetype="application/json")


@csrf_exempt
def signup(request):

    print '\n\nsignup'

    if request.method == 'POST':

        user_id = request.POST['user_id']
        pwd = request.POST['pwd']
        temp = ""

        print user_id+ " "+pwd

        try:
            temp = User.objects.get(user_id=user_id).email
        except Exception as e:
            print e

        if not temp == user_id:
            user = User(user_id=user_id, pwd=pwd)
            user.save()
            msg = "Signup Success"
            status = 1
        else:
            msg = "Email is already taken"
            status = 0
            #return HttpResponse(json.dumps(dict), mimetype="application/json", status=500)
        print "asd"

        dict = {'email': user_id, 'msg': msg, 'status': status}

        return HttpResponse(json.dumps(dict), mimetype="application/json")

    def user(request):

        print '\n\nUser\n\n'
        users = User.objects.all()

        for user in users:
            print user.email + " " + user.pwd

        HttpResponse("Hello World2")