"""
Description: A class meant to manage Mortgage options.
Author: Shiqi Yu
Date: 2023-11-10
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""


from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage():
    """
     This class will make use of the Enumerations and 
     List within the pixell_lookup.py file.
    """

    #__init__
    def __init__(self, Loan_Amount: float, 
                 Rate: MortgageRate, 
                 Frequency: PaymentFrequency, 
                 Amortization: int):
        """
        Initialize a new object with Loan_Amount,
        Rate, Frequency, Amortization.
        Args:
            Loan Amount (float): The amount of the mortgage loan.
            Rate (MortgageRate): The annual interest rate.
            Frequency (PaymentFrequency ): The number of payments per year.
            Amortization (int): The number of years to repay the mortgage loan.
        Returns:
            None
        Raises:
            ValueError: Loan Amount must be positive.
            ValueError: Rate provided is invalid.
            ValueError: Frequency provided is invalid.
            ValueError: Amortization provided is invalid.
        """
        if Loan_Amount > 0:
            self._Loan_Amount = Loan_Amount
        else:
            raise ValueError("Loan Amount must be positive.")
        
        if  isinstance(Rate, MortgageRate):
            self._Rate = Rate
        else:
            raise ValueError("Rate provided is invalid.")
        
        if isinstance(Frequency, PaymentFrequency):
            self._Frequency = Frequency
        else:
            raise ValueError("Frequency provided is invalid.")
        
        if Amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        else:
            self._Amortization = Amortization

    ## ACCESSORS
    @property
    def Loan_Amount(self) -> float:
        """
        Accessor for Loan_Amount attribute.
        """
        return self._Loan_Amount
    
    ## Mutator
    @Loan_Amount.setter
    def Loan_Amount(self, value: float):
        """
        Sets the loan amount.
        Args:
            incoming_value (): The amount.
        Raises:
            ValueError: When the value provided is 
            zero or negative.
        """
        if value > 0:
            self._Loan_Amount = value 
        else:
            raise ValueError("Loan Amount must be positive.")
    
    ## ACCESSORS
    @property
    def Rate(self) -> MortgageRate:
        """
        Accessor for Rate attribute.
        """
        return self._Rate
    
    ## Mutator
    @Rate.setter
    def Rate(self, value: MortgageRate):
        """
        Sets the Rate.
        Args:
            value (): The rate.
        Raises:
            ValueError: When Rate provided is invalid.
        """
        if isinstance(value, MortgageRate):
            self._Rate = value 
        else:
            raise ValueError("Rate provided is invalid.")
    
    ## ACCESSORS
    @property
    def Frequency(self) -> PaymentFrequency:
        """
        Accessor for frequency attribute.
        """
        return self._Frequency
    
    ## Mutator
    @Frequency.setter
    def Frequency(self, value: PaymentFrequency):
        """
        Sets the frequency.
        Args:
            value (): The frequency.
        Raises:
            ValueError: When frequency provided is invalid.
        """
        if isinstance(value, PaymentFrequency):
            self._Frequency = value 
        else:
            raise ValueError("Frequency provided is invalid.")
        
    ## ACCESSORS
    @property
    def Amortization(self) -> int:
        """
        Accessor for Amortization attribute.
        """
        return self._Amortization
    
    ## Mutator
    @Amortization.setter
    def Amortization(self, value: int):
        """
        Sets the Amortization.
        Args:
            value (): The value.
        Raises:
            ValueError: When Amortization provided is invalid.
        """
        if value not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        else:
            self._Amortization = value

    # Define calculate_payment method
    def calculate_payment(self) -> float:
        """
        Calculate the Weekly, BiWeekly or Monthly mortgage payment based on the details of the mortgage (amount, rate, frequency and amortization).
        This method should return the calculated payment value.
        """
        
        # Define variables
        P = self._Loan_Amount
        Frequency = self._Frequency.value
        I = (self._Rate.value/1)/self.Frequency.value
        Amortization = float(self._Amortization)
        N = float(Amortization*Frequency)
        Calculated_payment = P*(I*(1+I)**N)/((1+I)**N - 1)

        # return round(Calculated_payment, 2)
        return Calculated_payment

    def __str__(self):
        """
        Returns a string representation of the class.
        Returns:
            str:  A string representation of mortgage.
                format: Mortgage Amount:
                        Rate:
                        Amortization:
                        Frequency:
                example:
                        Mortgage Amount: $682,912.43
                        Rate: 5.89%
                        Amortization: 30
                        Frequency: Monthly -- Calculated Payment: $4,046.23  
        """
        return (f"Mortgage Amount: ${self._Loan_Amount:,.2f}"
                + f"\nRate: {self._Rate.value*100:,.2f}%"
                + f"\nAmortization: {self.Amortization}"
                + f"\nFrequency: {self.Frequency.name} -- Calculated Payment: ${self.calculate_payment():,.2f}")        

    def __repr__(self):
        """
        Provides a representation of an Mortgage objec.
        Returns:
                str: A representation of simple data.
                    format: loan_amount , rate , amortization, frequency
                    example: [682912.43, 0.0589, 30, 12]
            
            return (f"{self.account_type} | "
                    + f"{self.account_number} | "
                    + f"{self.balance}")
        """
        return (f"[{self._Loan_Amount}, {self._Rate.value}, {self._Amortization}, {self._Frequency.value}]")


     