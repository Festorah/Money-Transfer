from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	account_number = models.CharField(max_length=10, blank=True)
	opening_account_balance = models.IntegerField(blank=True, null=True)
	account_balance = models.IntegerField(blank=True, null=True)
	date_created = models.DateTimeField(default=timezone.now, blank=True, null=True)

	def __str__(self):
		return f"{self.user.username} Profile"


class Transaction(models.Model):

	sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_id', blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	date = models.DateTimeField(default=timezone.now)
	amount = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return f"{self.sender.username} Transaction"
