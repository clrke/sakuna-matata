from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse


@csrf_exempt
def home(request):
    if request.method == 'POST':
        return HttpResponse('Accepted')
