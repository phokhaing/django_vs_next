from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'staff_id',
        'fullname',
        'gender',
        'email',
        'is_active'
    ]