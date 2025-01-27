import csv

class OutputHandler:
    """
    Define a class that handle output.

    Attributes: account_summaries: a dictonary of account summary
                suspicious_transactions: a list of suspicious transaction
                transaction_statistics: a dictonary of transaction statistics.
        
    Methods :
        write_account_summaries_to_csv:
        write_suspicious_transactions_to_csv:
        write_transaction_statistics_to_csv:

    """

    def __init__(self, account_summaries: dict, 
                       suspicious_transactions: list, 
                       transaction_statistics: dict) -> None:
        """
         Initialize a new object 
        Args:
            account_summaries: dict
            suspicious_transactions: list
            transaction_statistics: dict
        Returns:
            None
        """
        self._account_summaries = account_summaries
        self._suspicious_transactions = suspicious_transactions
        self._transaction_statistics = transaction_statistics
    

    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """
        Write account sumarry to csv file.

        Args:
            file_path:  The path to the CSV file where the account summaries will be written.
        Returns:
            None
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])

            for account_number, summary in self._account_summaries.items():
                writer.writerow([
                    account_number,
                    summary['balance'],
                    summary['total_deposits'],
                    summary['total_withdrawals']
                ])

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """
            Write information about suspicious transactions to a CSV file.

         Args:
            file_path (str): The path to the CSV file where information about suspicious transactions will be written.

        Returns:
            None
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction ID', 'Account number', 'Date', 'Transaction type', 'Amount', 'Currency', 'Description'])

            for transaction in self._suspicious_transactions:
                writer.writerow([
                    transaction['Transaction ID'],
                    transaction['Account number'],
                    transaction['Date'],
                    transaction['Transaction type'],
                    transaction['Amount'],
                    transaction['Currency'],
                    transaction['Description']
                ])

    def write_transaction_statistics_to_csv(self, file_path: str) -> None:
        """
        Write information about transaction statistics to a CSV file.

        Args:
            file_path (str): The path to the CSV file where information about transaction statistics will be written.

        Returns:
            None
        """        
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction type', 'Total amount', 'Transaction count'])

            for transaction_type, statistic in self._transaction_statistics.items():
                writer.writerow([
                    transaction_type,
                    statistic['total_amount'],
                    statistic['transaction_count']
                ])

    def filter_account_summaries(self,filter_field: str ,filter_value: int ,filter_mode:bool) -> list:
        """
        Get data from account summaries and filters it and return the filtered_summaries 
        Args:
            filter_field (str): One of the following filter fields: "balance", "total_deposits" or "total_withdrawals".
            filter_value (int): An integer value to which the filter field will be compared.
            filter_mode (bool): The mode determines how to filter. 
                                    If it's True, number should be Greater than or Equal.  
                                    If it's False, number should be Less than or Equal.  
        return:
            filtered_summaries (list) : filtered summaries under the criteria written in filter_mode 
        """
        filtered_summaries = []
        for account_number, summary in self._account_summaries.items():
            if filter_mode:
                if summary.get(filter_field) >= filter_value:
                    filtered_summaries.append({
                        'account_number': account_number,
                        'balance': summary['balance'],
                        'total_deposits': summary['total_deposits'],
                        'total_withdrawals': summary['total_withdrawals']
                    })
            else:
                if summary.get(filter_field) <= filter_value:
                    filtered_summaries.append({
                        'account_number': account_number,
                        'balance': summary['balance'],
                        'total_deposits': summary['total_deposits'],
                        'total_withdrawals': summary['total_withdrawals']
                    })
        return filtered_summaries
    
    def write_filtered_summaries_to_csv(self, filtered_data: list, file_path: str) -> None:
        """
        Write filtered account summaries to a CSV file.
        Args:
            filtered_data (list): The data filtered by filter_account_summaries.
            file_path (str): The file name that data will be written.
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])

            for summary in filtered_data:
                writer.writerow([
                    summary['account_number'],
                    summary['balance'],
                    summary['total_deposits'],
                    summary['total_withdrawals']
                ])