from django.urls import path
from . import views


urlpatterns = [
    path('entrance/', views.entrance, name='entrance'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('manager/', views.employee_view, name='employee_view')
]
