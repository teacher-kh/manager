import json
from typing import List
from datetime import datetime
from models.transaction import Transaction
from utils.context import FileContext

class FileManager:
    @staticmethod
    def save_to_file(file_name: str, data: List[Transaction]):
        with FileContext(file_name, mode="w") as file:
            json.dump([transaction.to_dict() for transaction in data], file, indent=2)

    @staticmethod
    def load_from_file(file_name: str) -> List[Transaction]:
        with FileContext(file_name, mode="r") as file:
            data = json.load(file)
        
        return [Transaction.from_dict(item) for item in data]
