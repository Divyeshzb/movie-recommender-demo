import unittest
import re
import hashlib
import random

def get_rating(film_id):
    if not isinstance(film_id, int):
        raise TypeError("film_id must be an integer")
    h = hashlib.md5(str(film_id).encode('utf-8')).hexdigest()

    m = re.search("[012345]", h)
    digit = int(h[m.start()])
    if digit == 3:
        rating = random.randrange(1, 3)
    else:
        rating = random.randrange(3, 6)
    return rating

class TestGetRating(unittest.TestCase):

    def test_get_rating(self):
        # Test with a known film_id
        film_id = 123456
        rating = get_rating(film_id)
        # Check if rating is in expected range
        self.assertTrue(1 <= rating <= 5)

    def test_get_rating_with_invalid_input(self):
        # Test with a non-integer film_id
        film_id = "abc"
        with self.assertRaises(TypeError):
            get_rating(film_id)

    def test_get_rating_with_negative_input(self):
        # Test with a negative film_id
        film_id = -123456
        rating = get_rating(film_id)
        # Check if rating is in expected range
        self.assertTrue(1 <= rating <= 5)

if __name__ == '__main__':
    unittest.main()
