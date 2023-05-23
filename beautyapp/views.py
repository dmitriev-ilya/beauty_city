from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def notes(request):
    return render(request, 'notes.html')
