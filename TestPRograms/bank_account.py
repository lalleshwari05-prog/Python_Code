"""A simple bank account demonstration. Run: python bank_account.py"""

from decimal import Decimal, InvalidOperation


class BankAccount:
    """Store an account balance and its transaction history."""

    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.balance = Decimal("0.00")
        self.transactions = []

    @staticmethod
    def validate_amount(amount):
        try:
            amount = Decimal(str(amount))
        except InvalidOperation:
            raise ValueError("Enter a valid amount.") from None
        if not amount.is_finite() or amount <= 0:
            raise ValueError("Amount must be a positive, finite number.")
        if amount != amount.quantize(Decimal("0.01")):
            raise ValueError("Use no more than two decimal places.")
        return amount

    def deposit(self, amount):
        amount = self.validate_amount(amount)
        self.balance += amount
        self.transactions.append(f"Deposited ${amount:.2f}")
        print(f"Deposit successful. Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        amount = self.validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(f"Withdrew ${amount:.2f}")
        print(f"Withdrawal successful. Balance: ${self.balance:.2f}")

    def show_details(self):
        print(f"\nOwner: {self.owner}")
        print(f"Account number: {self.account_number}")
        print(f"Current balance: ${self.balance:.2f}")

    def show_history(self):
        print("\nTransaction history:")
        if not self.transactions:
            print("No transactions yet.")
        for number, transaction in enumerate(self.transactions, start=1):
            print(f"{number}. {transaction}")


def main():
    print("=== Bank Account Demo ===")
    owner = input("Enter account holder name: ").strip() or "Sample Customer"
    account = BankAccount(owner, "100001")

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Account details\n4. Transaction history\n5. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                account.deposit(input("Amount to deposit: ").strip())
            elif choice == "2":
                account.withdraw(input("Amount to withdraw: ").strip())
            elif choice == "3":
                account.show_details()
            elif choice == "4":
                account.show_history()
            elif choice == "5":
                print("Thank you. Goodbye!")
                break
            else:
                print("Please choose an option from 1 to 5.")
        except (ValueError, InvalidOperation) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
