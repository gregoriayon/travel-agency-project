# Generated by Django 4.2.2 on 2023-07-07 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        (
            "app_flight",
            "0005_rename_base_adult_fare_airplaneticketmodel_base_price_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="airplaneticketmodel",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="airplaneticketmodel",
            name="start_date",
        ),
        migrations.AddField(
            model_name="airplaneticketmodel",
            name="arrive_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="airplaneticketmodel",
            name="arrive_time",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="airplaneticketmodel",
            name="depart_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="airplaneticketmodel",
            name="depart_time",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
