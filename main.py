from models.transaction import Transaction
from services.budget_manager import BudgetManager
from services.file_manager import FileManager

def main():
    manager = BudgetManager()

    t1 = Transaction(amount=750, category="Salary", date='2024-10-23', description="Monthly salary")
    t2 = Transaction(amount=250, category="Groceries", date='2024-11-02', description="Weekly groceries")
    t3 = Transaction(amount=100, category="Vacation", date='2024-07-20', description="Saving for vacation")

    manager.add_transaction(t1)
    manager.add_transaction(t2)
    manager.add_transaction(t3)

    FileManager.save_to_file("transactions.json", manager.transactions)

    loaded_transactions = FileManager.load_from_file("transactions.json")

    print("Завантажені транзакції:")
    for transaction in loaded_transactions:
        print(transaction)

    print("\nКатегорії:")
    categories = manager.get_by_category()
    for category, transactions in categories.items():
        print(f"{category}: {transactions}")

    print("\nЗагальний баланс:", manager.calculate_balance())

if __name__ == "__main__":
    main()
