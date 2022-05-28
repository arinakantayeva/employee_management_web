from django.contrib import admin
from .models import UserDetail


@admin.register(UserDetail)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'iin', 'phone', 'email')
    list_filter = ('user', 'iin', 'phone', 'email')
    search_fields = ['user__username', 'iin', 'phone', 'email']
