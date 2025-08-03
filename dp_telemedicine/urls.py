
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('da_users.urls')),
    path('api/appointments/', include('da_appointments.urls')),
]
