import unittest
from unittest.mock import patch
from your_flask_app import models

# This import assumes that wtforms is installed
try:
    from wtforms import ValidationError
except ImportError:
    print("wtforms module is not installed. Install it with 'pip install wtforms'")
    raise

class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.user = models.User()

    @patch.object(models.User, 'email_is_registered')
    def test_validate_email_already_registered(self, mock_email_is_registered):
        mock_email_is_registered.return_value = True
        with self.assertRaises(ValidationError):
            self.user.validate_email('test@example.com')

    @patch.object(models.User, 'email_is_registered')
    def test_validate_email_not_registered(self, mock_email_is_registered):
        mock_email_is_registered.return_value = False
        try:
            self.user.validate_email('test@example.com')
        except ValidationError:
            self.fail("validate_email() raised ValidationError unexpectedly!")

if __name__ == '__main__':
    unittest.main()
