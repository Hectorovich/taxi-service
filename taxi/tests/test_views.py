from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from taxi.models import Driver


class PublicDriverTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get("taxi:car-list")

        self.assertNotEqual(response.status_code, 200)

    def test_create_login_required(self):
        response = self.client.get("taxi:car-form")

        self.assertNotEqual(response.status_code, 200)


class DriverSearchTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="es",
            password="1234test",
            first_name="Te",
            last_name="st",
            license_number="AAA12345"
        )
        self.client.force_login(self.user)

        driver1 = Driver.objects.create(
            username="test",
            password="1234test",
            first_name="Te",
            last_name="st",
            license_number="ABC12345"
        )
        driver2 = Driver.objects.create(
            username="Test",
            password="1234test",
            first_name="Te",
            last_name="st",
            license_number="ABB12346"
        )
        driver3 = Driver.objects.create(
            username="bes",
            password="1234test",
            first_name="Te",
            last_name="st",
            license_number="BBB02346"
        )

    def test_search_driver_by_username(self):
        response = self.client.get(reverse("taxi:driver-list") + "?search=t")
        driver = Driver.objects.filter(username__icontains="t")

        self.assertEqual(list(response.context["driver_list"]), list(driver))
