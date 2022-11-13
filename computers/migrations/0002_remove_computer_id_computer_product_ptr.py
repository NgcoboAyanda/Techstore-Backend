# Generated by Django 4.1.2 on 2022-11-13 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('computers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='id',
        ),
        migrations.AddField(
            model_name='computer',
            name='product_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.product'),
            preserve_default=False,
        ),
    ]
