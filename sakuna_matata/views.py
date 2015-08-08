from django.shortcuts import render, redirect
from api.models import Channel,Message

def home(request, name):
    channels = Channel.objects.all()
    messages = Message.objects.all()
    current_channel = Channel.objects.filter(name=name)
    if current_channel.count():
        current_channel = current_channel[0]
    else:
        current_channel = Channel.objects.all()[0]

    return render(request, 'home.html', {
        'channels': channels,
        'current_channel': current_channel,
        'messages' : messages
    })
