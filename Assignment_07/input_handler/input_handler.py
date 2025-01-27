import csv
import json

class InputHandler:
    """
    Define a class that handle input.

    Attributes: file_path: The file format
        
    Methods :
        get_file_format: get the format of a file
        read_input_data: read data file and return data
        read_csv_data: read and return csv file
        read_json_data: read and return json file 
    """
    def __init__(self, file_path: str):
        """
          Initialize a new object with file_path which is a str.
        Args:
           self._file_path: return file_path
        Returns:
            None
        """
        self._file_path = file_path


    def get_file_format(self) -> str:
        """
           Initialize a new method to get file format.
        Args:
           file.split:
        Returns:
            None
        """
        parts = self._file_path.split('.')
        if len(parts) > 1:
            return parts[-1]
        else:
            return ""

    def read_input_data(self) -> list:
        """
          Initialize a new method to read input data.
        Args:
           read file format, returrn data
        Returns:
            list
        """
        data = []
        file_format = self.get_file_format()
        if file_format == 'csv':
            data =  self.read_csv_data()
        elif file_format == 'json':
            data = self.read_json_data()

        return self.data_validation

    def read_csv_data(self) -> list:
        """
           Initialize a new method to read csv data.
        Args:
           
        Returns:
            list
        """
        input_data = []
        try:
            with open(self._file_path, 'r') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    input_data.append(row)
            return input_data
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self._file_path} does not exist.")

        

    def read_json_data(self) -> list:
        """
            Initialize a new method to read json data.
        Args:
           
        Returns:
            list
        """
        # Research the json.load function so that you 
        # understand the format of the data once it is
        # placed into input_data
        try:

            with open(self._file_path, 'r') as input_file:
                input_data = json.load(input_file)
                
            return input_data
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self._file_path} does not exist.")

    def data_validation(data: list) -> list:
        """
        Validates the input data and returns only the valid records.

            Parameters:
                data (list): The data to validate, where each item is a dictionary.

            Returns:
                list: A list containing only the valid dictionaries.
        """
        valid_data = []
        for row in valid_data:
            try:
                amount = float(row["Amount"])
                if amount < 0 :
                    continue

                 # Transaction type validation
                transaction_type = row['Transaction type'].lower()
                if transaction_type not in ['deposit', 'withdrawal', 'transfer']:
                    # Skip invalid transaction types
                    continue  

                valid_data.append(row)
            except (KeyError, ValueError, TypeError):
                # Skip records with missing fields or invalid data types
                continue

        return valid_data
