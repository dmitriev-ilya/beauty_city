from django.shortcuts import render

from .models import Saloon, Service


def index(request):
    salons = Saloon.objects.all()

    salon_details = []
    for salon in salons:
        salon_detail = {
            'name': salon.name,
            'city': salon.city,
            'address': salon.address,
            'image': salon.avatar.url if salon.avatar else None
        }
        salon_details.append(salon_detail)

    services = Service.objects.all()
    service_details = []
    for service in services:
        service_detail = {
            'name': service.name,
            'image': service.avatar.url,
            'price': round(service.price, 0)
        }
        service_details.append(service_detail)

    context = {
        'salons': salon_details,
        'services': service_details
    }

    return render(request, 'index.html', context=context)


def notes(request):
    return render(request, 'notes.html')


def view_service(request):
    return render(request, 'service.html')
