from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        FACTORY = "factory", "Factory/Industrial Operator"
        AGRICULTURE = "agriculture", "Agricultural Producer"
        ADMIN = "admin", "Platform Administrator"
        EXPORTER = "exporter", "Textile/Garment Exporter"
        RECYCLER = "recycler", "Recycling Facility Operator"
        LOGISTICS = "logistics", "Logistics Operator"

    role = models.CharField(max_length=20, choices=Role.choices)
    company_name = models.CharField(max_length=150, blank=True)
    is_verified = models.BooleanField(default=False)