from django.shortcuts import render

from .models import Saloon, Service, Master, Review


def index(request):
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

    reviews = Review.objects.filter(raiting__gte=4).select_related('note__user')
    review_details = []
    for review in reviews:
        review_detail = {
            'user_name': review.note.user.username,
            'text': review.text,
            'raiting': review.raiting,
            'date': review.created_at.strftime("%d.%m.%Y")
        }
        review_details.append(review_detail)

    context = {
        'salons': salon_details,
        'services': service_details,
        'masters': master_details,
        'reviews': review_details
    }

    return render(request, 'index.html', context=context)


def notes(request):
    return render(request, 'notes.html')


def view_service(request):
    return render(request, 'service.html')
