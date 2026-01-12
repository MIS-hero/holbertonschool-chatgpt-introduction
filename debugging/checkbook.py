#!/usr/bin/python3
"""
checkbook.py

A simple checkbook application that allows users to deposit money,
withdraw money, and check their current balance through a command-line
interface.
"""

class Checkbook:
    """
    Class Checkbook
    ----------------
    Represents a simple checkbook with a balance that can be modified
    through deposits and withdrawals.
    """

    def __init__(self):
        """
        Initializes the checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.

        Parameters:
        amount (float): The amount of money to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook if funds are sufficient.

        Parameters:
        amount (float): The amount of money to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Prompts the user for a valid monetary amount.

    Parameters:
    prompt (str): The message displayed to the user.

    Returns:
    float: A valid non-negative amount.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount must be non-negative.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """
    Main program loop that handles user interaction.
    """
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).lower()

        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
