# Generated by Django 3.1.4 on 2021-03-13 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('categories', models.CharField(choices=[('Beverage', 'Beverage'), ('Pasta', 'Pasta'), ('Cake', 'Cake'), ('Bakery', 'Bakery'), ('Sandwiches', 'Sandwiches')], max_length=50)),
                ('sizes', models.CharField(choices=[('Short', 'Short'), ('Tall', 'Tall'), ('Grande', 'Grande'), ('Venti', 'Venti')], max_length=50)),
                ('img', models.ImageField(upload_to=None)),
                ('description', models.TextField()),
                ('s_price', models.FloatField()),
                ('t_price', models.FloatField()),
                ('g_price', models.FloatField()),
                ('v_price', models.FloatField()),
                ('price', models.FloatField(default=None)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_quantity', models.IntegerField()),
                ('ordered', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.IntegerField()),
                ('reference_number', models.CharField(blank=True, default='6166234453', max_length=10, null=True, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('items', models.ManyToManyField(to='core.OrderItem')),
            ],
        ),
    ]
