"""
Description: A class used to test the Mortgage class.
Author: Shiqi Yu
Date: 2023-11-10
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
import unittest
from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

# Define the unit Test class by inheriting unittest.TestCase
class MortgageTests(unittest.TestCase):
    def test_invalid_Loan_Amount(self):
        # Arrange
        Rate = MortgageRate.FIXED_1
        Frequency = PaymentFrequency.BI_WEEKLY
        Amortization = 5
        Loan_Amount = -800
        expected = "Loan Amount must be positive."
        # Act and ASSERT
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        self.assertEqual(expected, str(context.exception))

    def test_invalid_rate(self):
        # Arrange
        Rate = "Invalid"
        Frequency = PaymentFrequency.MONTHLY
        Amortization = 5
        Loan_Amount = 800
        expected = "Rate provided is invalid."
        # Act and ASSERT
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount,Rate, Frequency, Amortization)
        self.assertEqual(expected, str(context.exception))

    def test_invalid_frequency(self):
        # Arrange
        Rate = MortgageRate.FIXED_5
        Frequency = 44
        Amortization = 5
        Loan_Amount = 800
        expected = "Frequency provided is invalid."
        # Act and ASSERT
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        self.assertEqual(expected, str(context.exception))

    def test_invalid_Amortization(self):
        # Arrange
        Rate = MortgageRate.FIXED_5
        Frequency = PaymentFrequency.BI_WEEKLY
        Amortization = 9
        Loan_Amount = 800
        expected = "Amortization provided is invalid."
        # Act and ASSERT
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        self.assertEqual(expected, str(context.exception))

    def test_init_all_valid_input(self):
        # Arrange
        Rate = MortgageRate.FIXED_5
        Frequency = PaymentFrequency.MONTHLY
        Amortization = 5
        Loan_Amount = 800
        # Act
        mortgage_account = Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        # Assert
        self.assertEqual(mortgage_account._Rate, Rate)
        self.assertEqual(mortgage_account._Frequency, Frequency)
        self.assertEqual(mortgage_account._Amortization, Amortization)
        self.assertEqual(mortgage_account.Loan_Amount, Loan_Amount)

    def test_loan_amount_accessor_valid(self):
        # Arrange
        Rate = MortgageRate.FIXED_5
        Frequency = PaymentFrequency.MONTHLY
        Amortization = 5
        Loan_Amount = 80
        expected = 80
        # Act and ASSERT
        mortgage_account = Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        self.assertEqual(expected, mortgage_account.Loan_Amount)

    def test_loan_amount_mutator_zero(self):
        # Arrange
        Rate = MortgageRate.FIXED_5
        Frequency = PaymentFrequency.MONTHLY
        Amortization = 5
        Loan_Amount = 78
        expected = "Loan Amount must be positive."
        account_mortgage = Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        # Act and ASSERT
        with self.assertRaises(ValueError) as context:
            account_mortgage.Loan_Amount = 0
        self.assertEqual(expected, str(context.exception))
    
    def test_loan_amount_mutator_negative(self):
        # Arrange
        Rate = MortgageRate.FIXED_5
        Frequency = PaymentFrequency.MONTHLY
        Amortization = 5
        Loan_Amount = 78
        expected = "Loan Amount must be positive."
        account_mortgage = Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        # Act and ASSERT
        with self.assertRaises(ValueError) as context:
            account_mortgage.Loan_Amount = -299
        self.assertEqual(expected, str(context.exception))

   
    def test_loan_amount_mutator_positive(self):
        # Arrange
        account = Mortgage(50,MortgageRate.VARIABLE_3,PaymentFrequency.MONTHLY, 5)
        expected = 100
        # Act
        account.Loan_Amount = 100
        # Assert
        self.assertEqual(expected, account.Loan_Amount)

    def test_rate_accessor_valid(self):
        # Arrange
        Rate = MortgageRate.FIXED_5
        Frequency = PaymentFrequency.MONTHLY
        Amortization = 5
        Loan_Amount = 800
        # Act
        mortgage_account = Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        # Assert
        self.assertEqual(mortgage_account.Rate, MortgageRate.FIXED_5)

    def test_rate_mutator_valid(self):
         # Arrange
        account = Mortgage(100,MortgageRate.VARIABLE_3,PaymentFrequency.MONTHLY, 5)
        expected = MortgageRate.FIXED_1
        # Act
        account.Rate = MortgageRate.FIXED_1
        # Assert
        self.assertEqual(expected, account.Rate)

    def test_rate_mutator_invalid(self):
        # Arrange
        mortgate_acount = Mortgage(100, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 15)
        expected = "Rate provided is invalid."
        # Act and ASSERT
        with self.assertRaises(ValueError) as context:
            mortgate_acount.Rate = "BI-YEARLY"
        self.assertEqual(expected, str(context.exception))

    def test_Frequency_accessor_valid(self):
        # Arrange and act
        account = Mortgage(12345, MortgageRate.VARIABLE_1, PaymentFrequency.WEEKLY, 30)
        expected = PaymentFrequency.WEEKLY
        # Assert
        self.assertEqual(expected, account.Frequency)

    def test_Frequency_mutator_invalid(self):
        # Arrange
        Rate = MortgageRate.FIXED_5
        Frequency = PaymentFrequency.BI_WEEKLY
        Amortization = 5
        Loan_Amount = 80
        expected = "Frequency provided is invalid."
        mortgage_account = Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        # Act and ASSERT
        with self.assertRaises(ValueError) as context:
            mortgage_account.Frequency = 0
        self.assertEqual(expected, str(context.exception))

    def test_Amortization_accessor_valid(self):
        # Arrange
        account = Mortgage(100,MortgageRate.VARIABLE_3,PaymentFrequency.MONTHLY, 5)
        expected = 5
        # Assert
        self.assertEqual(expected, account.Amortization)

    def test_Amortization_mutator_invalid(self):
        # Arrange
        Rate = MortgageRate.VARIABLE_1
        Frequency = PaymentFrequency.BI_WEEKLY
        Amortization = 15
        Loan_Amount = 55
        expected = "Amortization provided is invalid."
        mortgage_account = Mortgage(Loan_Amount, Rate, Frequency, Amortization)
        # Act and ASSERT
        with self.assertRaises(ValueError) as context:
            mortgage_account.Amortization = 80
        self.assertEqual(expected, str(context.exception))

 

    def test_calculate_payment_valid(self):
        # Arrange and Act
        customer1 = Mortgage(682912.43, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 30)
        # Assert
        self.assertAlmostEqual(customer1.calculate_payment(), 4046.23, 2)

    def test_str_monthly_payment(self):
        # Arrange
        customer1 = Mortgage(682912.43, MortgageRate.FIXED_1,PaymentFrequency.MONTHLY, 30)
        expected = (f"Mortgage Amount: $682,912.43"
                + f"\nRate: 5.89%"
                + f"\nAmortization: 30"
                + f"\nFrequency: MONTHLY -- Calculated Payment: $4,046.23")
        # Act
        actual = str(customer1)
        # Assert
        self.assertEqual(expected,actual)
    
    def test_str_biweekly_payment(self):
        # Arrange
        customer1 = Mortgage(682912.43, MortgageRate.FIXED_1,PaymentFrequency.BI_WEEKLY, 30)
        expected = (f"Mortgage Amount: $682,912.43"
                + f"\nRate: 5.89%"
                + f"\nAmortization: 30"
                + f"\nFrequency: BI_WEEKLY -- Calculated Payment: $1,866.60")
        # Act
        actual = str(customer1)
        # Assert
        self.assertEqual(expected,actual)

    def test_str_weekly_payment(self):
        # Arrange
        customer1 = Mortgage(682912.43, MortgageRate.FIXED_1,PaymentFrequency.WEEKLY, 30)
        expected = (f"Mortgage Amount: $682,912.43"
                + f"\nRate: 5.89%"
                + f"\nAmortization: 30"
                + f"\nFrequency: WEEKLY -- Calculated Payment: $933.11")
        # Act
        actual = str(customer1)
        # Assert
        self.assertEqual(expected,actual)

    def test_repr_valid(self):
        # Arrange
        customer = Mortgage(682912.43, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 30)
        expected = "[682912.43, 0.0589, 30, 12]"
        # Act
        actual = repr(customer)
        # Assert
        self.assertEqual(expected,actual)

