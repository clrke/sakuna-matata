from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse


@csrf_exempt
def home(request):
    if request.method == 'POST':
        if request.headers["message_type"] == "incoming":
            try:
                #request.headers["message"] do something with the messge here
                return HttpResponse('Accepted')
            except Exception:
                return HttpResponse('Error')
        else:
            return HttpResponse('Error')
    else:
        User.objects.create_superuser('angelhack', 'angelhack@mailinator.com', 'angelhack2015')
        return JsonResponse(User.objects.all()[0].email, safe=False)
