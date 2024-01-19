# Generated by Django 5.0 on 2024-01-18 21:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="accounts/images/")),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=10
                    ),
                ),
                ("mobile_no", models.CharField(max_length=12)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]