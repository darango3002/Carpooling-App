# Generated by Django 4.2.5 on 2023-12-18 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ride_finder", "0007_car_user_car_alter_ride_user_car"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ride",
            name="user_car",
        ),
        migrations.AddField(
            model_name="car",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="User_Car",
        ),
    ]