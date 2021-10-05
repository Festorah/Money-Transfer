from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Transaction
import string
import random

#Generating random unique Account number for the each profile
def account_number_generator(size=10, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		account_number = account_number_generator()
		Profile.objects.create(user=instance, account_number=account_number, opening_account_balance=5000, account_balance=5000)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()







