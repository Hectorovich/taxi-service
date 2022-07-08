from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="1234admin"
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="driver",
            password="1234driver",
            license_number="ABC12345"
        )

    def test_driver_license_number_listed(self):
        """Tests that driver`s license number is in list_display on driver admin page"""
        url = reverse("admin:taxi_driver_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.driver.license_number)

    def test_driver_detailed_license_number_listed(self):
        """Tests that driver`s license number is on driver detail page"""
        url = reverse("admin:taxi_driver_change", args=[self.driver.id])
        response = self.client.get(url)
        self.assertContains(response, self.driver.license_number)

    def test_driver_additional_info_listed(self):
        """Tests that driver`s additional info is on driver add page"""
        url = reverse("admin:taxi_driver_add")
        response = self.client.get(url)
        self.assertContains(response, "Additional info")
        self.assertContains(response, "first_name")
        self.assertContains(response, "last_name")
        self.assertContains(response, "license_number")
