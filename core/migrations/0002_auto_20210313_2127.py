# Generated by Django 3.1.4 on 2021-03-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='g_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='s_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='sizes',
            field=models.CharField(blank=True, choices=[('Short', 'Short'), ('Tall', 'Tall'), ('Grande', 'Grande'), ('Venti', 'Venti')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='t_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='v_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='reference_number',
            field=models.CharField(blank=True, default='6173742462', max_length=10, null=True, unique=True),
        ),
    ]
