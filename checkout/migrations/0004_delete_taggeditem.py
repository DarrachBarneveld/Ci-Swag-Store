# Generated by Django 4.2.8 on 2023-12-22 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_user_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaggedItem',
        ),
    ]
