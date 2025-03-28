import unittest
from unittest.mock import Mock
from src.data_service import DataService

class TestDataService(unittest.TestCase):

    def setUp(self):
        self.api_mock = Mock()
        self.service = DataService(self.api_mock)

    def test_fetch_user_data_positive(self):
        self.api_mock.get_data.side_effect = [{'name': 'Jan'}, {'name': 'Anna'}]
        result = self.service.fetch_user_data(123)
        self.assertEqual(result, {'name': 'Jan'})
        result2 = self.service.fetch_user_data(567)

        self.api_mock.get_data.assert_called()
        self.assertEqual(self.api_mock.get_data.call_count, 2)
        self.api_mock.get_data.assert_called_with(567)


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()