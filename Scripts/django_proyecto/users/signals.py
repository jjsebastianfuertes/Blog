# post_save signal when a user is created
from django.db.models.signals import post_save
# sender is waht is sending the signal
from django.contrib.auth.models import User
# receiver is a function that get the signal and preforms a task
from django.dispatch import receiver


from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
