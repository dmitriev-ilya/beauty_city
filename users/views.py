import json
import random

from .send_sms import send_auth_sms
from beauty_city.settings import SMS_KEY

from beautyapp.models import Note
from django.db.models import Sum

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from beautyapp.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone


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
    notes = Note.objects.all()
    total_notes_count = notes.count()
    month_notes_count = notes.filter(created_at__month=timezone.now().month).count()
    month_paid_orders_price = notes.filter(
        payment__isnull=False,
        created_at__month=timezone.now().month
    ).aggregate(Sum('price'))['price__sum']
    month_orders_price = notes.filter(created_at__month=timezone.now().month).aggregate(Sum('price'))['price__sum']
    paid_orders_share = round((month_paid_orders_price / month_orders_price) * 100, 0)
    total_payment_balance = notes.filter(payment__isnull=True).aggregate(Sum('price'))['price__sum']

    context = {
        'total_notes_count': total_notes_count,
        'month_notes_count': month_notes_count,
        'total_price': month_paid_orders_price,
        'paid_orders_share': paid_orders_share,
        'total_payment_balance': total_payment_balance
    }
    return render(request, 'manager.html', context)
