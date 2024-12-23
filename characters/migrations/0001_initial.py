# Generated by Django 5.1.4 on 2024-12-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Character",
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
                ("api_id", models.IntegerField(unique=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Alive", "Alive"),
                            ("Dead", "Dead"),
                            ("Unknown", "Unknown"),
                        ],
                        max_length=50,
                    ),
                ),
                ("species", models.CharField(max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Genderless", "Genderless"),
                            ("Unknown", "Unknown"),
                        ],
                        max_length=50,
                    ),
                ),
                ("image", models.URLField(max_length=255, unique=True)),
            ],
        ),
    ]
