class BankAccount:
    def __init__(self, acc_num, holder, initial_balance):
        # private attributes
        self.__account_number = acc_num
        self.__account_holder = holder
        self.__balance = 0
        self.__transactions = []

        # validate initial balance
        if initial_balance >= 0:
            self.__balance = initial_balance
            self.__transactions.append(f"Account created with balance {initial_balance}")
        else:
            print("Initial balance cannot be negative")

    # Read-only property for account number
    @property
    def account_number(self):
        return self.__account_number

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance with validation
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            self.__transactions.append(f"Balance set to {amount}")
        else:
            print("Balance cannot be negative")

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposited {amount}")
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            self.__transactions.append(f"Withdrew {amount}")
            print(f"Withdrawn: {amount}")

    # Display account info
    def display_account_info(self):
        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__account_holder)
        print("Balance:", self.__balance)

    # Show transaction history
    def show_transactions(self):
        print("\nTransaction History:")
        if not self.__transactions:
            print("No transactions yet.")
        else:
            for t in self.__transactions:
                print("-", t)


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    acc1 = BankAccount("12345", "Joseph", 1000)

    acc1.display_account_info()

    acc1.deposit(500)
    acc1.withdraw(200)
    acc1.withdraw(2000)  # Insufficient balance

    print("\nCurrent Balance:", acc1.get_balance())

    acc1.show_transactions()