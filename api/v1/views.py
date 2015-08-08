from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse


@csrf_exempt
def home(request):
    if request.method == 'POST':
        return HttpResponse('Accepted')
    else:
        User.objects.create_superuser('angelhack', 'angelhack@mailinator.com', 'angelhack2015')
        return JsonResponse(User.objects.all()[0].email, safe=False)
