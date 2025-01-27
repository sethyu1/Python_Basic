import unittest
from unittest import TestCase
from data_processor.data_processor import DataProcessor

class TestDataProcessor(TestCase):
    """The following constant has been provided to reduce the amount of 
    code needed when creating DataProcessor class objects in the tests that 
    follow.  To use the constant, prefix it with self.  Examples:
    self.INPUT_DATA
    e.g.:  data_procesor = DataProcessor(self.INPUT_DATA)
    """
    INPUT_DATA = [{"Transaction ID":"1" , "Account number":"1001" ,"Date":"2023-03-01" ,
                   "Transaction type": "deposit","Amount":1000,"Currency":"CAD","Description":"Salary"}, 
                {"Transaction ID":"2" ,"Account number":"1002" ,"Date":"2023-03-01" ,
                "Transaction type": "deposit","Amount":1500,"Currency":"CAD","Description":"Salary"},
                {"Transaction ID":"3" ,"Account number":"1003" ,"Date":"2023-03-01" ,
                "Transaction type": "withdrawal","Amount":1100,"Currency":"CAD","Description":"Salary"},
                {"Transaction ID":"4" ,"Account number":"1004" ,"Date":"2023-03-01" ,
                "Transaction type": "withdrawal","Amount":11000,"Currency":"CAD","Description":"Salary"},
                {"Transaction ID":"5" ,"Account number":"1005" ,"Date":"2023-03-01" ,
                "Transaction type": "deposit","Amount":2000,"Currency":"XRP","Description":"Salary"}]
    
    # def setUp(self):
    #    self.data.processor = DataProcessor(self.INPUT_DATA)
    
    def test_update_account_summary_deposit(self):
        # Arrange
        expected= {
                "account_number": "1001",
                "balance": 1000,
                "total_deposits": 1000,
                "total_withdrawals": 0
            }
        # Act
        data = DataProcessor(self.INPUT_DATA)
        data.update_account_summary(self.INPUT_DATA[0])
        # Assert
        actual_summary = data._account_summaries["1001"]
        self.assertEqual(actual_summary["balance"], expected["balance"])
        self.assertEqual(actual_summary["total_deposits"], expected["total_deposits"])
        self.assertEqual(actual_summary["total_withdrawals"], expected["total_withdrawals"])

    
    def test_update_account_summary_withdrawal(self):
        # Arrange
        expected= {
                "account_number": "1003",
                "balance": -1100,
                "total_deposits": 0,
                "total_withdrawals": 1100
            }
        # Act
        data = DataProcessor(self.INPUT_DATA)
        data.update_account_summary(self.INPUT_DATA[2])
        # Assert
        actual_summary = data._account_summaries["1003"]
        self.assertEqual(actual_summary["balance"], expected["balance"])
        self.assertEqual(actual_summary["total_withdrawals"], expected["total_withdrawals"])
        
    def test_check_suspicious_transactions_large_amount(self):
        # Arrange
        data =DataProcessor(self.INPUT_DATA)
        data.check_suspicious_transactions(self.INPUT_DATA[3])
        expected = [{"Transaction ID":"4" ,"Account number":"1004" ,"Date":"2023-03-01" ,
                "Transaction type": "withdrawal","Amount":11000,"Currency":"CAD","Description":"Salary"}]
        # Act and Assert
        suspicous_transactions = data._suspicious_transactions
        self.assertEqual(suspicous_transactions[0]["Amount"],11000)
        self.assertEqual(suspicous_transactions, expected)
        

    def test_check_suspicious_transactions_uncommon_currency(self):
        # Arrange
        data = DataProcessor(self.INPUT_DATA)
        data.check_suspicious_transactions(self.INPUT_DATA[4])
        expected = [{"Transaction ID":"5" ,"Account number":"1005" ,"Date":"2023-03-01" ,
                "Transaction type": "deposit","Amount":2000,"Currency":"XRP","Description":"Salary"}]
        # Act and Assert
        suspicous_transactions = data._suspicious_transactions
        self.assertEqual(suspicous_transactions[0]["Currency"],"XRP")
        self.assertEqual(suspicous_transactions, expected)

    def test_update_transacation_statistics(self):
        # Arrange
        data = DataProcessor(self.INPUT_DATA)
        data.update_transaction_statistics(self.INPUT_DATA[4])
        expected = {'deposit':{
                "total_amount": 2000,
                "transaction_count": 1
            }}
        # Act and Assert
        self.assertEqual(data._transaction_statistics, expected)
        
    def test_get_average_transaction_amount(self):
        # Arrange
        data = DataProcessor(self.INPUT_DATA)
        data.process_data()
        # Act
        average_deposit = data.get_average_transaction_amount("deposit")
        average_withdrawal = data.get_average_transaction_amount("withdrawal")
        # Assert
        self.assertEqual(average_deposit,1500)
        self.assertEqual(average_withdrawal,6050)
        



if __name__ == "__main__":
    unittest.main()