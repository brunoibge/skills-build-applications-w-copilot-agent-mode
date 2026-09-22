from django.test import TestCase
from rest_framework.test import APIClient

from .models import User


class OctofitApiTests(TestCase):
    def test_api_root_exposes_resources(self):
        response = APIClient().get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)
        self.assertTrue(response.data['users'].endswith('/api/users/'))

    def test_user_email_is_unique(self):
        User.objects.create(name='Hero', email='hero@example.com')
        with self.assertRaises(Exception):
            User.objects.create(name='Copy', email='hero@example.com')

    def test_user_ids_are_serialized_as_strings(self):
        User.objects.create(name='Hero', email='hero@example.com')
        response = APIClient().get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)
        self.assertIsInstance(response.data[0]['id'], str)