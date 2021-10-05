from rest_framework import serializers

from home.models import *


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'

