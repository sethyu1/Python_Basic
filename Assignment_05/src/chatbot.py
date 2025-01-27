"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: Shiqi Yu
Date: 2023-10-25
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:

def get_account():
    """
    Prompt user to enter an account number, return the number or raise an exception if it is incorrect.
    Args:
        account_number = input("Please enter your account number:")
    Returns:
        account number
    Raises:
        raise ValueError("Account number entered does not exist.") if the account is intger but not in the dictionary.
        raise ValueError("Account number must be a whole number.") if the account is not intger.
    """
    try: 
        account_number = input("Please enter your account number:")
        account_number = int(account_number)
    except ValueError:
            raise ValueError("Account number must be a whole number.")
        
    if account_number not in ACCOUNTS:  
        raise ValueError("Account number does not exist.")
    return account_number
   

def get_amount()-> float:
    """
    Prompt user to enter transaction amount, return the number or raise an exception if it is incorrect.
    Args:
        account_amount = input("Please enter the transaction amount:")
    Returns:
        account amount
    Raises:
        raise ValueError("Invalid amount. Please enter a positive number.") if the amount is negative or zero.
        raise ValueError("Invalid amount. Amount must be numeric.") if the amount is not number.
    """
    
    account_amount = input("Please enter the transaction amount:")
    try:
        account_amount = float(account_amount)
    except ValueError:
        raise ValueError("Invalid amount. Amount must be numeric.")
        
    if account_amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")

    return account_amount
def get_balance(account: int) -> str:
    """
    Retrieve the balance of user account
    Args:
        account_number = input("Please enter your account number:")
    Returns:
        
    Raises:
        raise ValueError("Account number does not exist.") if the account does not exist.
    """
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    else:
        balance = ACCOUNTS[account]["balance"]
        return(f"Your current balance for account {account} is ${balance:,.2f}.")
def make_deposit(account: int, amount: float) -> str:
    """
    Prompt user to enter account and deposit amount, print the outcome.
    Args:
        account
        amount 
    Returns:
        return(f"You have made a deposit of ${new_balance:,.2f} to account {account_number}.")
    Raises:
        raise ValueError("Account number does not exist.")
        raise ValueError("Invalid Amount. Amount must be positive.")
    """
    
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
        
    if amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")
    else:    
        ACCOUNTS[account]["balance"] += amount
        new_balance = ACCOUNTS[account]["balance"]
        return(f"You have made a deposit of ${amount:,.2f} to account {account}.")

def user_selection() -> str:
    """
    Prompt user to select three options, return the outcome
    Args:
        selection = input
    Returns:
        return selection
    Raises:
        raise ValueError("Invalid task. Please choose balance, deposit, or exit.")
    """
    try:
        selection = input("What would you like to do (balance/deposit/exit)").lower()
        if selection not in VALID_TASKS:
           raise ValueError("Invalid task. Please choose balance, deposit, or exit.")
    except Exception as e:
        raise e 
    return selection


## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION

def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:
            selection = user_selection()
            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:
                        account = get_account()

                        valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:
                        outcome = get_balance(account)
                        print(outcome)
                       
                    
                else:
                    # Deposit
                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:
                            amount= get_amount()

                            valid_amount = True
                        except Exception as e:
                            # Invalid amount.
                            print(e)
                    ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                    ## VARIABLES account AND amount DEFINED ABOVE AND 
                    ## PRINT THE RESULTS:
                    result = make_deposit(account, amount)
                    print(result)


            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
if __name__ == "__main__":
    chatbot()
