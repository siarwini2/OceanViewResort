from django.test import TestCase
from django.urls import reverse
from .models import User


class AccountTests(TestCase):
    def test_superuser_becomes_admin(self):
        u = User.objects.create_superuser("boss", password="x")
        self.assertEqual(u.role, User.Role.ADMIN)

    def test_staff_is_not_django_admin(self):
        u = User.objects.create_user("ana", password="x")
        self.assertFalse(u.is_staff)
        self.assertFalse(u.is_hotel_admin)

    def test_login_redirects(self):
        User.objects.create_user("ana", password="pass12345")
        r = self.client.post(reverse("accounts:login"), {"username": "ana", "password": "pass12345"})
        self.assertEqual(r.status_code, 302)
