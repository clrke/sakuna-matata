from math import sqrt
from django.shortcuts import render
from api.models import Channel, Message

MAX_RADIUS = 0.05


def distance(xi, x):
    cx = (xi[0] - x[0]) ** 2
    cy = (xi[1] - x[1]) ** 2

    if cx + cy != 0:
        return sqrt(cx + cy)
    else:
        return 0


def home(request, name):
    channels = Channel.objects.all()
    threshold = int(request.GET['threshold']) if 'threshold' in request.GET else 999
    current_channel = Channel.objects.filter(name=name)
    if current_channel.count():
        current_channel = current_channel[0]
        messages = current_channel.message_set.all()
    else:
        messages = Message.objects.all()

    for message in messages:
        center = (message.latitude, message.longitude)
        message.total_sentiment = 0
        for message2 in messages:
            if distance((message2.latitude, message2.longitude), center) < MAX_RADIUS:
                message.total_sentiment += message.sentiment

    messages = sorted(messages, key=lambda m: m.total_sentiment)

    messages = [message for message in messages if message.total_sentiment <= threshold]

    return render(request, 'home.html', {
        'channels': channels,
        'name': name,
        'messages': messages,
        'threshold': threshold,
    })
