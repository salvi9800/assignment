from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    if kwargs.get('created', True):
        profile = Profile.objects.get_or_create(user=instance)
        
post_save.connect(create_profile, sender= User, dispatch_uid= "create_profile")
