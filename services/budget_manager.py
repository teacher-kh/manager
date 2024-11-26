from datetime import datetime
from typing import List, Dict
from collections import defaultdict
from models.transaction import Transaction

class BudgetManager:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def calculate_balance(self) -> float:
        return sum(t.amount for t in self.transactions)

    def get_by_category(self) -> Dict[str, List[Transaction]]:
        result = defaultdict(list)
        for transaction in self.transactions:
            result[transaction.category].append(transaction)
        return dict(result)

    def filter_transactions(
        self, 
        start_date: datetime = None, 
        end_date: datetime = None, 
        category: str = None, 
        min_amount: float = None, 
        max_amount: float = None
    ) -> List[Transaction]:
        filtered = self.transactions.copy()
        
        if start_date:
            filtered = [t for t in filtered if t.date >= start_date]
        
        if end_date:
            filtered = [t for t in filtered if t.date <= end_date]
        
        if category:
            filtered = [t for t in filtered if t.category == category]
        
        if min_amount is not None:
            filtered = [t for t in filtered if t.amount >= min_amount]
        
        if max_amount is not None:
            filtered = [t for t in filtered if t.amount <= max_amount]
        
        return filtered

    def generate_monthly_summary(self, year: int, month: int) -> Dict:
        monthly_transactions = self.filter_transactions(
            start_date=datetime(year, month, 1),
            end_date=datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
        )
        
        category_totals = defaultdict(float)
        for transaction in monthly_transactions:
            category_totals[transaction.category] += transaction.amount
        
        return {
            'total_income': sum(t.amount for t in monthly_transactions if t.amount > 0),
            'total_expense': abs(sum(t.amount for t in monthly_transactions if t.amount < 0)),
            'categories': dict(category_totals)
        }
