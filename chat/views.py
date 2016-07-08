# import random
# import string
# from django.db import transaction
# from django.shortcuts import render, redirect,HttpResponse
# import haikunator
# from .models import Room
# from django.contrib.auth.decorators import login_required
#
# def about(request):
#     return render(request, "chat/about.html")
#
# def new_room(request):
#     """
#     Randomly create a new room, and redirect to it.
#     """
#     new_room = None
#     while not new_room:
#         with transaction.atomic():
#             label = haikunator.haikunate()
#             if Room.objects.filter(label=label).exists():
#                 continue
#             new_room = Room.objects.create(label=label)
#     return redirect(chat_room, label=label)
#
#
# @login_required()
# def chat_room(request, label):
#     """
#     Room view - show the room, with latest messages.
#
#     The template for this view has the WebSocket business to send and stream
#     messages, so see the template for where the magic happens.
#     """
#     # If the room with the given label doesn't exist, automatically create it
#     # upon first visit (a la etherpad).
#     room, created = Room.objects.get_or_create(label=label)
#
#     # We want to show the last 50 messages, ordered most-recent-last
#     messages = reversed(room.messages.order_by('-timestamp')[:50])
#     return render(request, "chat/room.html", {
#         'room': room,
#         'messages': messages,
#     })
#
#

import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
import haikunator
from .models import Room
from project.models import Project
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import string
@login_required()
def test(request):
    return HttpResponse("Hello World")

def about(request):
    return render(request, "chat/about.html")

def new_room(request):
    """
    Randomly create a new room, and redirect to it.
    """
    new_room = None
    while not new_room:
        with transaction.atomic():
            label =  "".join( [random.choice(string.letters) for i in xrange(15)] )
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
    return redirect(chat_room, label=label)

@login_required
def chat_room(request, label):
    """
    Room view - show the room, with latest messages.

    The template for this view has the WebSocket business to send and stream
    messages, so see the template for where the magic happens.
    """
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    print(request.user)
    print(label)
    print("chat room loaded")
    if request.user.is_authenticated():
        print("authenticated_user")
    room, created = Room.objects.get_or_create(label=label)
    try:
        project = Project.objects.get(room=room)
    except:

        return HttpResponseRedirect('/new/')
    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    if True :

        return render(request, "chat/room.html", {
            'room': room,
            'messages': messages,
        })
    else:

        return HttpResponseRedirect('/accounts/login/')


@login_required()
def testView(request):
        return HttpResponse("Gello world")

