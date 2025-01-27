import unittest
import csv
from unittest import TestCase
from unittest.mock import mock_open, patch
from output_handler.output_handler import OutputHandler


class TestOutputHandler(TestCase):
    """The following constants have been provided to reduce the amount of 
    code needed when creating OutputHandler class objects in the tests that 
    follow.  To use the constants, prefix them with self.  Examples:
    self.ACCOUNT_SUMMARIES
    self.SUSPICIOUS_TRANSACTIONS
    self.TRANSACTION_STATISTICS
    """

    ACCOUNT_SUMMARIES = { '1001': {'account_number': '1001', 'balance': 50, 
                            'total_deposits': 100, 'total_withdrawals': 50},
                            '1002': {'account_number': '2', 'balance': 200, 
                            'total_deposits': 200, 'total_withdrawals': 0}}
    
    SUSPICIOUS_TRANSACTIONS = [{"Transaction ID":"1" ,"Account number":"1001" ,
                            "Date":"2023-03-14" ,"Transaction type": "deposit",
                            "Amount":250,"Currency":"XRP","Description":"crypto investment"}  ]

    TRANSACTION_STATISTICS = {'deposit': {'total_amount': 300, 'transaction_count': 2}, 
                            'withdrawal': {'total_amount': 50, 'transaction_count': 1}}
    
    
    def setUp(self):
        self.handler = OutputHandler(
            self.ACCOUNT_SUMMARIES,
            self.SUSPICIOUS_TRANSACTIONS,
            self.TRANSACTION_STATISTICS
        )

    @patch('builtins.open', new_callable=mock_open)
    def test_write_account_summaries_to_csv(self, mock_file):
        file_path = 'account_summaries.csv'
        self.handler.write_account_summaries_to_csv(file_path)
        mock_file.assert_called_once_with(file_path, 'w', newline='')

        handle = mock_file()
        # The header row plus one row for each account summary
        expected_row_count = 1 + len(self.ACCOUNT_SUMMARIES)
        self.assertEqual(handle.write.call_count, expected_row_count)
    
    @patch('builtins.open', new_callable=mock_open)
    def test_write_suspicious_transactions_to_csv(self, mock_file):
        file_path = 'suspicious_transactions.csv'
        self.handler.write_suspicious_transactions_to_csv(file_path)
        mock_file.assert_called_once_with(file_path, 'w', newline='')

        handle = mock_file()
        # The header row plus one row for each suspicious transaction
        expected_row_count = 1 + len(self.SUSPICIOUS_TRANSACTIONS)
        self.assertEqual(handle.write.call_count, expected_row_count)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_transaction_statistics_to_csv(self, mock_file):
        file_path = 'transaction_statistics.csv'
        self.handler.write_transaction_statistics_to_csv(file_path)
        mock_file.assert_called_once_with(file_path, 'w', newline='')

        handle = mock_file()
        # The header row plus one row for each type of transaction statistic
        expected_row_count = 1 + len(self.TRANSACTION_STATISTICS)
        self.assertEqual(handle.write.call_count, expected_row_count)
        
            








if __name__ == "__main__":
    unittest.main()