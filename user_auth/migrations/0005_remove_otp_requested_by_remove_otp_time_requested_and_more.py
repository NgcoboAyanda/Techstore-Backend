# Generated by Django 4.1 on 2022-10-11 19:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='otp_request_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]