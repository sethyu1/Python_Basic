"""
Description:
Author: Shiqi Yu    
Date:  2023-10-25
Usage: Test the funciont in chatbot.py
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount,get_balance,make_deposit, user_selection     
from src.chatbot import ACCOUNTS, VALID_TASKS

class ChatbotTests(unittest.TestCase):
    def test_get_account_validility(self):
        with patch('builtins.input') as mock_input:
            # Arrage   
            mock_input.side_effect = ["123456"]
            expected = 123456
            # Act
            actual = get_account()
            # Assert
        self.assertEqual(actual, expected)
    def test_get_account_non_numeric(self):
        with patch('builtins.input') as mock_input:
            # Arrage   
            mock_input.side_effect = ["abcdef"]
            expected = "Account number must be a whole number."
            # Act
            with self.assertRaises(Exception) as context:
                get_account()
            # Assert
        self.assertEqual(expected,str(context.exception))

    def test_get_account_does_not_exist(self):
        with patch('builtins.input') as mock_input:
            # Arrage   
            mock_input.side_effect = ["112233"]
            expected = "Account number does not exist."
            # Act
            with self.assertRaises(Exception) as context:
                get_account()
            # Assert
        self.assertEqual(expected,str(context.exception))
    def test_get_amount_valid(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["500.01"]
            expected = 500.01
            # Act
            actual = get_amount()
            # Assert
            self.assertEqual(actual, expected)
    def test_get_amount_non_numeric(self):
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["abcdef"]
            expected = "Invalid amount. Amount must be numeric."
            # Act
            with self.assertRaises(Exception) as context:
                get_amount()
            # Assert
            self.assertEqual(expected,str(context.exception))
    def test_get_amount_zero(self):
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["0"]
            expected = "Invalid amount. Please enter a positive number."
            # Act
            with self.assertRaises(Exception) as context:
                get_amount()
            # Assert
            self.assertEqual(expected,str(context.exception))
    def test_get_balance_valid(self):
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["123456"]
            expected = "Your current balance for account 123456 is $1,000.00."
            # Act
            actual = get_balance(123456)
            # Assert
            self.assertEqual(expected,actual)
    def test_get_balance_account_does_not_exist(self):
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["112233"]
            expected = "Account number does not exist."
            # Act
            with self.assertRaises(Exception) as context:
                get_balance(112233)
            # Assert
            self.assertEqual(expected,str(context.exception))
    def test_make_deposit_correct(self):
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["123456","1500.01"]
            expected = 'You have made a deposit of $1,500.01 to account 123456.'
            # Act
            actual = make_deposit(123456, 1500.01)
            # Assert
            self.assertEqual(expected,actual)
    def test_make_deposit_balance_updated(self):
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["123456","1500.01"]
            expected = 2500.01
            # Act
            make_deposit(123456, 1500.01)
            actual = ACCOUNTS[123456]["balance"]
            # Assert
            self.assertEqual(expected,actual)
    def test_make_deposit_account_not_exist(self):
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["112233","1500.01"]
            expected = "Account number does not exist."
            # Act
            with self.assertRaises(Exception) as context:
                make_deposit(112233, 1500.01)
            # Assert
            self.assertEqual(expected,str(context.exception))
    def test_make_deposit_amount_less_than_zero(self):
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["123456","-50.01"]
            expected = "Invalid Amount. Amount must be positive."
            # Act
            with self.assertRaises(Exception) as context:
                make_deposit(123456, -50.01)
            # Assert
            self.assertEqual(expected,str(context.exception))
    def test_use_selection_valid(self):
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["balance"]
            expected = "balance"
            # Act
            actual = user_selection()
            # Assert
            self.assertEqual(expected, actual)
    def test_use_selection_wrong_case(self):
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["DEPOSIT"]
            expected = "deposit"
            # Act
            actual = user_selection()
            # Assert
            self.assertEqual(expected, actual)
    def test_use_selection_invalid(self):
        with patch('builtins.input') as mock_input:
            #Arrange
            mock_input.side_effect = ["CREATE"]
            expected = "Invalid task. Please choose balance, deposit, or exit."
            # Act
            with self.assertRaises(Exception) as context:
                user_selection()
            # Assert
            self.assertEqual(expected,str(context.exception))

