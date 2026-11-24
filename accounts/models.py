from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        STAFF = "staff", "Staff"
        ADMIN = "admin", "Admin"

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STAFF)
    phone = models.CharField(max_length=20, blank=True)

    @property
    def is_hotel_admin(self):
        return self.role == self.Role.ADMIN

    def save(self, *args, **kwargs):
        # Keep role and Django's flags in sync.
        # createsuperuser sets is_superuser, so treat that as an admin.
        if self.is_superuser:
            self.role = self.Role.ADMIN
        if self.role == self.Role.ADMIN:
            self.is_staff = True  # allows access to /admin/
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"

