# Generated by Django 4.1 on 2022-12-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0002_alter_desktop_os_alter_desktop_ram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='gpu',
            field=models.CharField(default='Integrated Graphics', max_length=100),
        ),
        migrations.AddField(
            model_name='laptop',
            name='gpu',
            field=models.CharField(default='Integrated Graphics', max_length=100),
        ),
    ]
