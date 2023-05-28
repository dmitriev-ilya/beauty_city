import json
import random

from .send_sms import send_auth_sms
from beauty_city.settings import SMS_KEY

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from beautyapp.models import User
from django.contrib.auth.hashers import make_password


@csrf_exempt
def entrance(request):
    if request.method == 'POST':
        if not request.POST:
            body_data = json.loads(request.body)
            if 'tel' in body_data and 'code' not in body_data:
                code = str(random.randint(1000, 9999))

                # send_auth_sms(SMS_KEY, body_data['tel'], code)
                print(code)
                User.objects.update_or_create(
                    username=body_data['tel'],
                    defaults={
                        'password': make_password(code),
                    }
                )
            if ('tel' and 'code') in body_data:
                user = authenticate(
                    request,
                    username=body_data['tel'],
                    password=body_data['code']
                )
                if user:
                    login(request, user)
                    return JsonResponse({'success': True}, status=200)

                return JsonResponse({'success': False}, status=403)

    return redirect('index')


def logout_view(request):
    logout(request)
    return render(request, 'index.html')


def is_employee(user):
    return user.is_staff


@user_passes_test(is_employee)
def employee_view(request):
    return render(request, 'manager.html')
