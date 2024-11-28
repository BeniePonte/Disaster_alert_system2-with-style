from django.contrib import admin
from .models import Alert, DisasterAlert, UserProfile

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'timestamp')  # Only include fields that exist in the Alert model
    search_fields = ('type', 'description')  # Optional: add fields you want searchable
    list_filter = ('type',)  # Filter by type as an example

@admin.register(DisasterAlert)
class DisasterAlertAdmin(admin.ModelAdmin):
    list_display = ('type', 'location', 'severity', 'timestamp')
    list_filter = ('type', 'severity')
    search_fields = ('type', 'location', 'description')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'location', 'is_staff', 'is_superuser')
    list_filter = ('location', 'is_staff')
    search_fields = ('username', 'email')
