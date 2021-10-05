from django.contrib import admin
from django.db import models
from .models import Profile, Transaction

admin.site.site_header = 'Kristina Bank'

admin.site.register(Transaction)
admin.site.register(Profile)