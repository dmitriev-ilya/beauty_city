import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        if request.POST:
            print(1)
        if not request.POST:
            body_data = json.loads(request.body)
            print(body_data)

    return render(request, 'index.html')


def notes(request):
    return render(request, 'notes.html')


def view_service(request):
    return render(request, 'service.html')
