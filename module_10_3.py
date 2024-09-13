import threading
import time
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.deposit_count = 0
        self.withdraw_count = 0

    def deposit(self):
        while self.deposit_count < 100:  # Fix 1: Use < instead of <= to avoid infinite loop
            amount = randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += amount
                self.deposit_count += 1
                print(f"Top-up: {amount}. Balance: {self.balance} ")
            finally:
                self.lock.release()
            time.sleep(0.001)

    def withdraw(self):
        while self.withdraw_count < 100:  # Fix 1: Use < instead of <= to avoid infinite loop
            amount = randint(50, 500)
            print(f"Request for {amount} ")
            self.lock.acquire()
            try:
                if self.balance >= amount:
                    self.balance -= amount
                    self.withdraw_count += 1
                    print(f"Withdrawal: {amount}. Balance: {self.balance}")
                else:
                    print(f"Request rejected, insufficient funds")
            finally:
                self.lock.release()
            time.sleep(0.001)


# Create an instance of the Bank class
bk = Bank()

# Fix 2: Pass instance methods to threads instead of class methods
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.withdraw)

# Start the threads
th1.start()
th2.start()

# Wait for both threads to finish
th1.join()
th2.join()

# Print the final balance
print(f'Final balance: {bk.balance}')
