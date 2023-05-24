from django.shortcuts import render

from .models import Saloon


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

    context = {
        'salons': salon_details
    }

    return render(request, 'index.html', context=context)


def notes(request):
    return render(request, 'notes.html')


def view_service(request):
    return render(request, 'service.html')
