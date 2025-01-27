"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Shiqi Yu
Date: 2023-11-10
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

VALID_AMORTIZATION = [5, 10, 15, 20, 25, 30] 

# Define a class
class MortgageRate(Enum):

    """
    An enumeration of the Mortgage rate 
    storing the value of fixed and variable 1,3,5 respectively
    Value:
    FIXED_5 = 0.0500
    FIXED_3 = 0.0579
    FIXED_1 = 0.0589
    VARIABLE_5 = 0.0650
    VARIABLE_3 = 0.0660
    VARIABLE_1 = 0.0679
    """
    FIXED_5 = 0.0500
    FIXED_3 = 0.0579
    FIXED_1 = 0.0589
    VARIABLE_5 = 0.0650
    VARIABLE_3 = 0.0660
    VARIABLE_1 = 0.0679

# Define another class
class PaymentFrequency(Enum):

    """
    An enumeration of the Payment frequency 
    of three different types.
    Value:
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52


