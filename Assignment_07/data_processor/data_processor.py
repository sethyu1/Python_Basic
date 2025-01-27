import logging
# Define a class
class DataProcessor:
    """
    A class that maintains methods to process date.

    Attributes:
        _input_data(list): initilize a list.

    Methods :
        process_data(): Modifies data and return a dictionary.
        update_account_summary(): Add new account number to account summary
        check_suspicious_transactions(): Spot the suspicious transactions and update to the suspicious transaction list.
        update_transaction_statistics(): Renew the transaction statistics.
        get_average_transaction_amount(): Caculate the average of transaction amount
    """

    LARGE_TRANSACTION_THRESHOLD = 10000
    UNCOMMON_CURRENCIES = ['XRP', 'LTC']

    def __init__(self, input_data: list,
                 logging_level = logging.info,
                 logging_format ='%(asctime)s - %(levelname)s - %(message)s',
                 logging_name = None ):
        """
         Initialize a new object with input_data, it is a list.
         Initialize logging level to __init__ method.
         Initialize logging format to __init__ method.
         Initialize log file to __init__ method.
        Args:
            self._input_data: the list of original data
            self._account_summaries: a dictionary of summaries of account
            self._suspicious_transactions: a list of suspicious transactions.
            self._transaction_statistics: a dictionary of transaction statistics.
        Returns:
            None
        """
        logging.basicConfig(level=logging.DEBUG,
        filename='app.log', 
        filemode='w', 
        format='%(asctime)s - %(levelname)s - %(message)s')            
                
        self.logger = logging.getLogger(__name__)
       
        self._input_data = input_data
        self.logging_level = logging_level
        self.logging_format = logging_format
        self.logging_name = logging_name

        self._account_summaries = {}
        self._suspicious_transactions = []
        self._transaction_statistics = {}

    def process_data(self) -> dict:
        """
        Process date from the input_data and return a dictionary with three attributes.

        Args:
            update_account_summary
            check_suspicious_transactions
            update_transaction_statistics
        Returns:
            {"account_summaries": self._account_summaries,
            "suspicious_transactions": self._suspicious_transactions,
            "transaction_statistics": self._transaction_statistics }
        """
        for row in self._input_data:
            self.update_account_summary(row)
            self.check_suspicious_transactions(row)
            self.update_transaction_statistics(row)

        # incorporate the logging messages, level info
        self.logger.info("Data Processing Complete.")

        return {
            "account_summaries": self._account_summaries,
            "suspicious_transactions": self._suspicious_transactions,
            "transaction_statistics": self._transaction_statistics
        }
    
        

    def update_account_summary(self, row: dict) -> None:
        """
        Update the account summarty dict: creat new account number and add amount to the balance 
        or deduct amount to the balance
        Args:
            add new account number if account number is not in account_summaries.
            add amount to the balance if transaction type is deposit.
            deduct amount to the balance if the transaction type is withdrawal and add to the total withdrawals.
        Returns:
            None
        """
        account_number = row['Account number']
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        # incorporate the logging messages, level info
        self.logger.info(f"Account summary updated: {account_number}")

        if account_number not in self._account_summaries:
            self._account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }

        if transaction_type == "deposit":
            self._account_summaries[account_number]["balance"] += amount
            self._account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self._account_summaries[account_number]["balance"] -= amount
            self._account_summaries[account_number]["total_withdrawals"] += amount

    def check_suspicious_transactions(self, row: dict) -> None:
        """
        Check the suspicious transactions: amount that is above 10000 or currency donominated by XRP OR LTC.
        add the suspicious transactions to the suspicious transaction list.
        Args:
            amount: amount from the dictionary.
            currency: currency from the dictionary.
        Returns:
            None
        """
        amount = float(row['Amount'])
        currency = row['Currency']

        # incorporate the logging messages, level warning
        self.logger.warning(f"Suspicious transaction: {row}")
        
        if amount > self.LARGE_TRANSACTION_THRESHOLD or currency in self.UNCOMMON_CURRENCIES:
            self._suspicious_transactions.append(row)

    def update_transaction_statistics(self, row: dict) -> None:
        """
        Update the transaction statistic if transaction type is not in transaction statistics
        and renew the total amount and transaction count in the new transaction type.
        Args:
            transaction type: from the dictionary.
            amount: amount from the dictionary.
        Returns:
            None
        """
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        # incorporate the logging messages, level info
        self.logger.info(f"Updated transaction: {transaction_type}")

        if transaction_type not in self._transaction_statistics:
            self._transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }

        self._transaction_statistics[transaction_type]["total_amount"] += amount
        self._transaction_statistics[transaction_type]["transaction_count"] += 1

    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        Caculate the average of transaction amount by deviding the total amount by transaction count.
        Args:
            total amount: total amount from transaction statistics
            transaction count: transaction count from transaction statistics
        Returns:
            average transaction amount(float)
        """
        total_amount = self._transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self._transaction_statistics[transaction_type]["transaction_count"]

        if transaction_count == 0:
            average = 0
        else:
            average = total_amount / transaction_count
        
        return average