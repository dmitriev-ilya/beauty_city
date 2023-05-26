from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from beautyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('notes/', views.notes, name='notes'),
    path('service/', views.view_service, name='service'),
    path('service-final/', views.view_service_final, name='service-final'),
    path('', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
