import unittest
from flask import Flask, session, url_for
from flask_login import login_user, logout_user, current_user
from your_flask_app import app, models  # Ensure 'your_flask_app' module exists in your project
from your_flask_app.forms import LoginForm, RegistrationForm  # Corrected import paths
from your_flask_app.auth import logout  # Corrected import paths

class TestLogout2fc1550d01(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_logout_success(self):
        with self.client:
            response = self.client.post(url_for('auth.login'), data=dict(
                username='test', password='test'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(current_user.name == 'test')
            self.assertTrue(current_user.is_authenticated)

            response = self.client.get(url_for('auth.logout'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertFalse(current_user.is_authenticated)

    def test_logout_without_login(self):
        with self.client:
            response = self.client.get(url_for('auth.logout'), follow_redirects=True)
            self.assertEqual(response.status_code, 302)  # Should redirect to login page
            self.assertFalse(current_user.is_authenticated)

if __name__ == '__main__':
    unittest.main()
