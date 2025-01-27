import unittest, os
from unittest import TestCase, mock
from unittest.mock import mock_open, patch
from input_handler.input_handler import InputHandler

class InputHandlerTests(TestCase):
    def test_get_file_format_proper_extension(self):
        # Arrange: Test with a file having a proper extension like .csv
        file_path_csv = InputHandler("input_data.csv")
        expected = "csv"
        # Act
        result_csv = file_path_csv.get_file_format()
        # Assert
        self.assertEqual(result_csv, expected)

    def test_get_file_format_empty_str(self):
        # Arrange: Test with a file without extension 
        file_path_csv = InputHandler("input_data")
        expected = ""
        # Act
        result_csv = file_path_csv.get_file_format()
        # Assert
        self.assertEqual(result_csv, expected)

    def setUp(self):
        # Create a temporary CSV file for testing with data
        self.temp_csv_path = "temp_test_data.csv"
        with open(self.temp_csv_path, 'w') as temp_file:
            temp_file.write("Name,Age,Gender\nJohn,25,Male\nJane,30,Female")

        # Create a temporary empty CSV file for testing
        self.temp_empty_csv_path = "temp_empty_test_data.csv"
        with open(self.temp_empty_csv_path, 'w') as temp_empty_file:
            # Leave the file empty
            temp_empty_file = None
            
        # Create a temporary file with an invalid extension for testing
        self.temp_invalid_file_path = "temp_invalid_data.txt"
        with open(self.temp_invalid_file_path, 'w') as temp_invalid_file:
            temp_invalid_file.write("This is an invalid file.") 

    def tearDown(self):
        # Remove the temporary CSV files after the tests
        if os.path.exists(self.temp_csv_path):
            os.remove(self.temp_csv_path)

        if os.path.exists(self.temp_empty_csv_path):
            os.remove(self.temp_empty_csv_path)
        
        if os.path.exists(self.temp_invalid_file_path):
            os.remove(self.temp_invalid_file_path)

    def test_read_csv_data_populated_list(self):
        # Arrange: Create an instance of InputHandler with the temporary CSV file
        input_handler = InputHandler(self.temp_csv_path)

        # Act: Call the read_csv_data method
        result_data = input_handler.read_csv_data()

        # Assert: Check if the result is a populated list
        self.assertIsInstance(result_data, list, "Result should be a list")
        self.assertGreater(len(result_data), 0, "List should be populated")

    def test_read_csv_data_empty_list(self):
        # Arrange: Create an instance of InputHandler with the temporary empty CSV file
        input_handler = InputHandler(self.temp_empty_csv_path)

        # Act: Call the read_csv_data method
        result_data = input_handler.read_csv_data()

        # Assert: Check if the result is an empty list
        self.assertIsInstance(result_data, list, "Result should be a list")
        self.assertEqual(len(result_data), 0, "List should be empty")

    def test_read_csv_data_file_not_found(self):
        # Arrange: Create an instance of InputHandler with a non-existent CSV file
        non_existent_file_path = "non_existent_file.csv"
        input_handler = InputHandler(non_existent_file_path)

        # Act and Assert: Check if FileNotFoundError is raised when calling read_csv_data
        with self.assertRaises(FileNotFoundError) as context:
            input_handler.read_csv_data()

        # Assert the specific error message if needed
        expected_error_message = f"File: {non_existent_file_path} does not exist."
        self.assertEqual(str(context.exception), expected_error_message)

        # read_input_data: Test to verify that a populated list is returned when a valid .csv file is used
    def test_read_input_data_valid_csv(self):
        # Arrange: Create an instance of InputHandler with the temporary CSV file
        input_handler = InputHandler(self.temp_csv_path)

        # Act: Call the read_input_data method
        result_data = input_handler.read_input_data()

        # Assert: Check if the result is a populated list
        self.assertIsInstance(result_data, list, "Result should be a list")
        self.assertGreater(len(result_data), 0, "List should be populated")

    @mock.patch('input_handler.input_handler.InputHandler.get_file_format', return_value='invalid')
    def test_read_input_data_invalid_extension(self, mock_get_file_format):
        # Arrange: Create an instance of InputHandler with the temporary file with an invalid extension
        input_handler = InputHandler(self.temp_invalid_file_path)

        # Act: Call the read_input_data method
        result_data = input_handler.read_input_data()

        # Assert: Check if the result is an empty list
        self.assertIsInstance(result_data, list, "Result should be a list")
        self.assertEqual(len(result_data), 0, "List should be empty")

    @patch('builtins.open', new_callable=mock_open, read_data='name,age\nAlice,30\nBob,25\nJason,45')
    def test_read_csv_data_with_data(self, mock_file):
        file_path = 'input/input_data.csv'
        input_handler = InputHandler(file_path)
        data = input_handler.read_csv_data()
        self.assertTrue(len(data) > 0)
        self.assertEqual(data, [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'},{'name': 'Jason', 'age': '45'}])

    def test_data_validation_excludes_non_numeric_amount(self):
        input_handler = InputHandler('input_data.csv')
        mock_data = [
            {'Amount': '1000', 'Transaction type': 'deposit'},  # Valid record
            {'Amount': 'abc123', 'Transaction type': 'withdrawal'}  # Non-numeric amount
        ]
        valid_data = input_handler.data_validation(mock_data)
        self.assertEqual(len(valid_data), 1)  # Only one valid record should remain
        self.assertEqual(valid_data[0]['Amount'], '1000')  # The valid record has amount '1000'

    def test_data_validation_negative_amount(self):
        input_handler = InputHandler('input_data.csv')
        mock_data = [
             {'Amount': '1000', 'Transaction type': 'deposit'},  # Valid record
            {'Amount': '-8000', 'Transaction type': 'withdrawal'}  # negative amount
        ]
        valid_data = input_handler.data_validation(mock_data)
        self.assertEqual(len(valid_data),1) 
        self.assertEqual(valid_data[0]['Amount'], '1000')

    def test_data_exclude_invalid_transaction_type(self):
        input_handler = InputHandler('input_data.csv')
        mock_data = [
            {'Amount': '1000', 'Transaction type': 'deposit'},  # Valid record
            {'Amount': '8000', 'Transaction type': 'open'}  # invalid transaction type
        ]
        valid_data = input_handler.data_validation(mock_data)
        self.assertEqual(len(valid_data), 1)   # Valid record
        self.assertEqual(valid_data[0]['Amount'], '1000')  # invalid transaction type

        
if __name__ == "__main__":
    unittest.main()