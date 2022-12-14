# Generated by Django 4.1 on 2022-12-30 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.product')),
                ('size', models.CharField(max_length=100)),
                ('os', models.CharField(default='Windows 10', max_length=50)),
                ('ram', models.CharField(default='8GB', max_length=10)),
                ('storage', models.CharField(default='512GB SSD', max_length=10)),
                ('gpu', models.CharField(default='Integrated Graphics', max_length=100)),
            ],
            bases=('shop.product',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.product')),
                ('battery', models.CharField(default='5000mAh', max_length=100)),
                ('camera', models.CharField(default='720p', max_length=50)),
                ('os', models.CharField(default='Windows 10', max_length=50)),
                ('ram', models.CharField(default='8GB', max_length=10)),
                ('storage', models.CharField(default='512GB SSD', max_length=10)),
                ('gpu', models.CharField(default='Integrated Graphics', max_length=100)),
            ],
            bases=('shop.product',),
        ),
    ]
