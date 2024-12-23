from django.db import models


class Character(models.Model):
    class StatusChoices(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        Unknown = "Unknown"

    class GenderChoices(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        GENDERLESS = "Genderless"
        UNKNOWN = "Unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    species = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GenderChoices.choices)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name
