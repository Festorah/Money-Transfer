# Generated by Django 3.2.7 on 2021-10-04 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='opening_account_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
