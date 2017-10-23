from django.shortcuts import render
from django.contrib.auth.models import User
from random import randint
from django.views import generic

from .forms import NewSession
from .models import Session
from .models import Chat

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        context={}
    )

def SessionView(request):
    if request.method == 'GET':
        id = request.GET.get('id', '')
        chat = request.GET.get('chat', '')
    session = Session.objects.get(id=id)
    if chat != '':
        Chat.objects.create(session=session, chat=chat)
    return render(
        request,
        'session.html',
        context={
            'session': session
        }
    )

def LoadingView(request):
    if request.method == 'GET':
        homeTeam = request.GET.get('homeTeam', '')
        awayTeam = request.GET.get('awayTeam', '')
    session = Session.objects.create(homeTeam=homeTeam, awayTeam=awayTeam)
    return render(
        request,
        'loading.html',
        context={'id': session.id}
    )
