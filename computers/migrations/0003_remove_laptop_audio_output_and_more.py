# Generated by Django 4.1 on 2022-12-01 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0002_rename_battey_laptop_battery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='audio_output',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='connectivity',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='video_output',
        ),
    ]
