from django.contrib.auth.models import AbstractUser
from django.db import models

# Model for generic alerts
class Alert(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

# Model for disaster alerts
class DisasterAlert(models.Model):
    TYPE_CHOICES = [
        ('flood', 'Flood'),
        ('earthquake', 'Earthquake'),
        ('storm', 'Storm'),
        ('wildfire', 'Wildfire'),
        ('hurricane', 'Hurricane'),
        ('other', 'Other'),
    ]

    SEVERITY_CHOICES = [
        (1, 'Low'),
        (2, 'Moderate'),
        (3, 'High'),
        (4, 'Severe'),
        (5, 'Extreme'),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    location = models.CharField(max_length=255)
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} at {self.location} (Severity: {dict(self.SEVERITY_CHOICES).get(self.severity)})"

# Custom user model with additional profile data
class UserProfile(AbstractUser):
    LOCATION_CHOICES = [
        ('girne', 'Girne'),
        ('lefkoşa', 'Lefkoşa'),
        ('lefke', 'Lefke'),
        ('iskele', 'İskele'),
        ('gazimağusa', 'Gazimağusa'),
        ('güzelyurt', 'Güzelyurt'),
    ]

    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, blank=True)

    def __str__(self):
        return f"User Profile for {self.username}"
