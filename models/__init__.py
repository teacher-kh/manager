from models.transaction import Transaction

def main():
    t1 = Transaction(amount=756, category="Salary", date="2024-10-25")
    t2 = Transaction(amount=-250, category="Groceries", date="2024-11-01")

    print(t1)
    print(t2)

if __name__ == "__main__":
    main()
