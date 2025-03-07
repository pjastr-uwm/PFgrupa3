import unittest
from src.email import validate_email


class TestEmail(unittest.TestCase):

    def setUp(self):
        pass

    def test_validate_positive(self):
        # self.assertEqual(validate_email("info@wp.pl"), True)
        self.assertTrue(validate_email("info@wp.pl"))

    def test_validate_negative(self):
        self.assertFalse(validate_email("xyz"))

    def test_integer_argument(self):
        with self.assertRaises(TypeError):
            validate_email(67889)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
