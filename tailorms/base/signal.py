from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import  User
from .models import Profile
from django.utils import timezone
from django.dispatch import receiver



def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != "":
        user.username = user.email

 
pre_save.connect(updateUser, sender=User,)


def profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user = instance,
            name = instance.username,
            role='customer'
      
        ) 
        print('profile created ')

post_save.connect(profile, sender=User)