# Generated by Django 4.1 on 2022-12-12 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0004_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.product')),
                ('screen_size', models.CharField(max_length=10)),
                ('battery', models.CharField(max_length=100)),
                ('camera', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=10)),
                ('storage', models.CharField(max_length=10)),
            ],
            bases=('shop.product',),
        ),
    ]