from django.shortcuts import render
from django.contrib.auth.models import User
from random import randint

from .forms import NewSession
from .models import Session

# Create your views here.
def index(request):
    info = 'testing'
    if request.method == 'POST':
        form = NewSession(request.POST)
    else:
        form = NewSession(request.GET)
        if form.is_valid():
            form = form.cleaned_data['response']
    return render(
        request,
        'index.html',
        context={'info':info,'form':form}
    )

def SessionView(request):
    sessions = []
    if request.method == 'GET':
        try:
            id = request.GET['id']
        except:
            id = ''
    if not sessions:
        sessions.append(Session(0, 'Home1', 'Away1'))
    else:
        sessions.append(Session(1, 'Home2', 'Home2'))
    return render(
        request,
        'session.html',
        context={'name': sessions[0].home}
    )

def LoadingView(request):
    session = Session.objects.create(homeTeam='home', awayTeam='away')
    sessionNum = Session.objects.all().count()
    return render(
        request,
        'loading.html',
        context={'num': sessionNum}
    )
