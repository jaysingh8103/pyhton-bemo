import sys
import json
import os

class Customer:
    Bank_name = "HDFC Bank"
    def __init__(self, name, account_num, account_balance=0):
        self.name = name
        self.account_num = account_num
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        print("Total Account Balance is:", self.account_balance)
        self.save_to_json()

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient Balance")
            sys.exit()
        self.account_balance -= amount
        print("Balance after Withdraw is:", self.account_balance)
        self.save_to_json()

    def check_balance(self):
        print("Account Balance is:", self.account_balance)

    def save_to_json(self):
        filename = "data.json"

        # Load existing data if the file exists
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                try:
                    customer_data = json.load(file)
                except json.JSONDecodeError:
                    customer_data = []
        else:
            customer_data = []

        # Update or add customer data
        updated = False
        for customer in customer_data:
            if customer["account_num"] == self.account_num:
                customer["account_balance"] = self.account_balance
                updated = True
                break
        if not updated:
            customer_data.append({
                "name": self.name,
                "account_num": self.account_num,
                "account_balance": self.account_balance
            })

        with open(filename, 'w') as json_file:
            json.dump(customer_data, json_file, indent=4)
            print(f"Data saved to {filename}")

    @staticmethod
    def load_previous_data():
        filename = "data.json"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                try:
                    customer_data = json.load(file)
                    if customer_data:
                        print("\nPrevious Customers Data:")
                        print("=" * 50)
                        for customer in customer_data:
                            print(f" Name: {customer['name']}, Account Number: {customer['account_num']}, Balance: {customer['account_balance']}")
                        print("=" * 50)
                    else:
                        print("\nNo previous data found.")
                except json.JSONDecodeError:
                    print("\nError reading previous data.")
        else:
            print("\nNo previous data file found.")
print("Welcome to", Customer.Bank_name)


Customer.load_previous_data()
name = input("\nEnter your name: ")
account_num = int(input("Enter your account number: "))


filename = "data.json"
existing_balance = 0

if os.path.exists(filename):
    with open(filename, 'r') as file:
        try:
            customer_data = json.load(file)
            for customer in customer_data:
                if customer["account_num"] == account_num:
                    existing_balance = customer["account_balance"]
                    print(f"Welcome back, {name}! Your current balance is: {existing_balance}")
                    break
        except json.JSONDecodeError:
            pass
print("=" * 50)
print("Customer name:", name)
print("Customer Account number:", account_num)
print("=" * 50)
c = Customer(name, account_num, existing_balance)
while True:
    print("\nOptions:")
    print("D - Deposit")
    print("W - Withdraw")
    print("C - Check Balance")
    print("E - Exit")
    print("=" * 50)

    option = input("Choose an option: ").strip().lower()

    if option == "d":
        amount = int(input("Enter the amount to deposit: "))
        c.deposit(amount)

    elif option == "w":
        amount = int(input("Enter the amount to withdraw: "))
        c.withdraw(amount)

    elif option == "c":
        c.check_balance()

    elif option == "e":
        print("Thank you for banking with us! Have a great day. ")
        sys.exit()

    else:
        print(" Invalid input! Please enter a valid option.")
