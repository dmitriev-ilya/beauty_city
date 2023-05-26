from django.shortcuts import render
from django.utils import timezone

from .models import Saloon, Service, Master, Review, Note
from django.contrib.auth.decorators import login_required

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


@login_required
def notes(request):
    user = request.user
    notes = Note.objects.filter(user=user).select_related('service', 'saloon', 'payment', 'master')
    note_details = []
    total_price = 0
    for note in notes:
        payment_status = 'НЕОПЛАЧЕНО'
        if note.payment and note.payment.status == 'Оплачен':
            payment_status = 'ОПЛАЧЕНО'
        note_detail = {
            'note_id': note.pk,
            'service_image': note.service.avatar.url,
            'notes__main_address': note.saloon.address,
            'note_payment_status': payment_status,
            'note_service_name': note.service.name,
            'note_master_name': note.master.full_name,
            'note_service_price': round(note.price, 0),
            'note_date_time': f'{note.date.strftime("%d.%m")} - {note.stime.strftime("%H:%M")}',
            'note_time_position': 'ПРОШЕДШИЕ' if (timezone.now().date() > note.date and timezone.now().time() > note.stime) else 'ПРЕДСТОЯЩИЕ'
        }
        note_details.append(note_detail)
        if payment_status == 'НЕОПЛАЧЕНО':
            total_price += note_detail['note_service_price']

    context = {
        'notes': note_details,
        'total_price': round(total_price, 0)
    }

    return render(request, 'notes.html', context)


def view_service(request):
    return render(request, 'service.html')
