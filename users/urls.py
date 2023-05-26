from django.urls import path
from . import views


urlpatterns = [
    path('my_view/', views.my_view, name='my_view'),
    path('logout_view/', views.logout_view, name='logout_view')
]
