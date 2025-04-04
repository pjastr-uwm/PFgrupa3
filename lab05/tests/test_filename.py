import unittest
from unittest.mock import patch
from datetime import datetime
from src.filename import generate_unique_filename

class TestFilename(unittest.TestCase):

    @patch("src.filename.datetime")
    def test_format_positive(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 2, 29, 3, 4,5)
        result = generate_unique_filename()
        self.assertEqual(result, "file_20240229_030405.txt")