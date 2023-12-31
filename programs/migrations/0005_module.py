# Generated by Django 3.2.23 on 2023-12-13 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_program_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='programs.program')),
            ],
        ),
    ]
