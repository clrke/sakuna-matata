from django.contrib.auth.models import User
from django.core.management.commands import migrate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from api.models import Message, Channel
import requests
from sakuna_matata import settings


@csrf_exempt
def home(request):
    if request.method == 'POST':
        message_split = request.POST['message'].split('&|!')
        mobile_number = request.POST['mobile_number']

        channel_name = message_split[0]
        latitude = message_split[1]
        longitude = message_split[2]
        description = message_split[3]
        contents = message_split[4]

        channel = Channel.objects.filter(name=channel_name)

        if not channel:
            channel = Channel(name=channel_name)
            channel.save()
        else:
            channel = channel[0]

        sentiment = int(requests.get('%s?message=%s' % (settings.SENTIMENT_ANALYSIS_URL, contents)).text)

        message = Message(
            channel=channel,
            latitude=float(latitude),
            longitude=float(longitude),
            description=description,
            message=contents,
            mobile_number=mobile_number,
            sentiment=sentiment,
        )

        message.save()
        return HttpResponse('Accepted')

    else:
        return JsonResponse(User.objects.all()[0].email, safe=False)
