from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.sessions.backends.db import SessionStore

from .forms import UserForm

def user_login(request):
    value = request.session.get("value", None)
    print(request.session.modified, value)
    if value:
        request.session['value'] = value+1
    else:
        request.session['value'] = 1
    if request.session.modified:
        request.session.save()
        print(request.session.session_key)
    userform = UserForm()
    return render(request, "user_auth/index.html", {
        "userform": userform,
    })
    