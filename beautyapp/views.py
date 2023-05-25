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

from .models import Saloon, Service, Master


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

    salons = Saloon.objects.all()

    salon_details = []
    for salon in salons:
        salon_detail = {
            'name': salon.name,
            'city': salon.city,
            'address': salon.address,
            'image': salon.avatar.url if salon.avatar else None,
            'opening_time': salon.opening_time.strftime("%H:%M"),
            'closing_time': salon.closing_time.strftime("%H:%M")
        }
        salon_details.append(salon_detail)

    services = Service.objects.all()
    service_details = []
    for service in services:
        service_detail = {
            'name': service.name,
            'image': service.avatar.url if service.avatar else None,
            'price': round(service.price, 0)
        }
        service_details.append(service_detail)

    masters = Master.objects.all().select_related('speciality')
    master_details = []
    for master in masters:
        master_detail = {
            'full_name': master.full_name,
            'avatar': master.avatar.url if master.avatar else None,
            'review_count': master.review_count,
            'speciality': master.speciality.name,
            'work_experience': master.work_experience
        }
        master_details.append(master_detail)

    context = {
        'salons': salon_details,
        'services': service_details,
        'masters': master_details
    }

    return render(request, 'index.html', context=context)


def notes(request):
    return render(request, 'notes.html')


def view_service(request):
    return render(request, 'service.html')
