import json
import random

from .send_sms import send_auth_sms
from beauty_city.settings import SMS_KEY

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import User
from django.contrib.auth.hashers import make_password


@csrf_exempt
def index(request):
    if request.method == 'POST':
        if request.POST:
            print(1)
        if not request.POST:
            body_data = json.loads(request.body)
            if 'tel' in body_data and 'code' not in body_data:
                code = str(random.randint(1000, 9999))

                # Включать эту функцию только при тестах с Тимуром (смс платные)
                # send_auth_sms(SMS_KEY, body_data['tel'], code)
                User.objects.update_or_create(
                    username=body_data['tel'],
                    defaults={
                        'phone_number': body_data['tel'],
                        'password': make_password(code),
                        'code': code,
                    }
                )
            if ('tel' and 'code') in body_data:
                user = authenticate(
                    request,
                    username=body_data['tel'],
                    password=body_data['code']
                )
                print(user)
                login(request, user)
                if user:
                    return JsonResponse({'success': True}, status=200)
                else:
                    return JsonResponse({'success': False}, status=403)

    return render(request, 'index.html')


def notes(request):
    return render(request, 'notes.html')


def view_service(request):
    return render(request, 'service.html')
