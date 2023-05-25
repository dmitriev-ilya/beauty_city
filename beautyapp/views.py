import json
import random

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User


@csrf_exempt
def index(request):
    if request.method == 'POST':
        if request.POST:
            print(1)
        if not request.POST:
            body_data = json.loads(request.body)
            print(body_data)
            if 'tel' in body_data and 'code' not in body_data:
                code = random.randint(1000, 9999)
                User.objects.update_or_create(
                    username=body_data['tel'],
                    defaults={
                        'phone_number': body_data['tel'],
                        'code': code
                    }
                )
            if ('tel' and 'code') in body_data:
                user = User.objects.get(username=body_data['tel'])
                if str(user.code) == body_data['code']:
                    print('Succes!')

    return render(request, 'index.html')


def notes(request):
    return render(request, 'notes.html')


def view_service(request):
    return render(request, 'service.html')
