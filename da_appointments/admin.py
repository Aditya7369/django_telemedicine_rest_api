from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'status', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ('patient__username', 'doctor__username')
    ordering = ('-timestamp',)
