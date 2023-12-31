# Generated by Django 4.2.8 on 2023-12-27 11:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_default_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
