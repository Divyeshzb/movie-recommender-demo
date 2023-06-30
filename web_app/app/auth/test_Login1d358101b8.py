import unittest
from flask import Flask
from your_flask_app import create_app, db
from your_flask_app.models import User

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
        db.create_all()

        # Create a user for the tests
        u = User(email='test@example.com', password='correct_password')
        db.session.add(u)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.session.drop_all()
        self.app_context.pop()

    def test_login_with_valid_credentials(self):
        response = self.client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'correct_password'
        }, follow_redirects=True)

        # The response should be a redirect to the main.index view
        self.assertTrue(b'Welcome' in response.data)

    def test_login_with_invalid_credentials(self):
        response = self.client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'wrong_password'
        }, follow_redirects=True)

        # The response should be the login page with an error message
        self.assertTrue(b'Invalid username or password' in response.data)

if __name__ == '__main__':
    unittest.main()
