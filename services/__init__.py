from models.transaction import Transaction
from services.budget_manager import BudgetManager

def main():
    manager = BudgetManager()
    t1 = Transaction(amount=750, category="Salary", date='2024-10-23')
    t2 = Transaction(amount=250, category="Groceries", date='2024-11-02')

    manager.add_transaction(t1)
    manager.add_transaction(t2)

    print(f"Balance: {manager.calculate_balance()}")
    
    categories = manager.get_by_category()
    for category, transactions in categories.items():
        print(f"Category: {category}: {transactions}")

if __name__ == "__main__":
    main()
