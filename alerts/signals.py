from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import DisasterAlert, UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

@receiver(post_save, sender=DisasterAlert)
def send_location_based_notification(sender, instance, created, **kwargs):
    if created:  # Only notify when a new alert is created
        # Fetch users with matching locations
        users_to_notify = UserProfile.objects.filter(location=instance.location)

        for user in users_to_notify:
            send_mail(
                subject=f"Disaster Alert: {instance.type}",
                message=f"A {instance.type} disaster has been reported in {instance.location}.",
                from_email='your-email@example.com',
                recipient_list=[user.email],
            )