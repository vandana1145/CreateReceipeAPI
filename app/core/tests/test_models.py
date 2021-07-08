from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):


    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfull"""
        email = 'vandana1145@gmail.com'
        password = 'Vandy@1287'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'vandana1145@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'Vandy@1287')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email or invalid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Vandy@1287')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'vandana1145@gmail.com',
            'Vandy@1287'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)