from django.db import models
from da_users.models import CustomUser

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    doctor = models.ForeignKey(CustomUser, related_name='appointments_as_doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey(CustomUser, related_name='appointments_as_patient', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.patient.username} with {self.doctor.username} on {self.timestamp.strftime('%Y-%m-%d %H:%M')} [{self.status}]"
