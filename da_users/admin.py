# da_users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_online', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
