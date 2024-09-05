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
        while self.deposit_count <= 100:
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
        while self.withdraw_count <= 100:
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

bk = Bank()

# Since the methods accept self, the Bank class object itself must be passed to the threads
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.withdraw, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Final balance: {bk.balance}')
