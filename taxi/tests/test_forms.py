from django.test import TestCase

from taxi.forms import DriverCreationForm, DriverLicenseUpdateForm


class FormsDriverTests(TestCase):
    def test_driver_creation_form(self):
        form_data = {
            "username": "user_test",
            "first_name": "test1",
            "last_name": "test2",
            "license_number": "ASD12345",
            "password1": "useruser098",
            "password2": "useruser098"
        }
        form = DriverCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_correct_license_update_form(self):
        form_data = {
            "license_number": "ASD12345"
        }
        form = DriverLicenseUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_incorrect_license_update_form(self):
        form_data = {
            "license_number": "asd1234"
        }
        form = DriverLicenseUpdateForm(data=form_data)

        self.assertFalse(form.is_valid())
