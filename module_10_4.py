from threading import Thread
import random
import time
from queue import Queue

# Table class: Represents a table in the cafe
class Table:
    def __init__(self, number):
        self.number = number  # Table number
        self.guest = None  # Guest seated at the table (None by default)

# Guest class: Represents a guest, which runs as a thread
class Guest(Thread):
    def __init__(self, name):
        super().__init__()  # Initialize the Thread class
        self.name = name  # Guest's name

    def run(self):
        # Simulate the guest eating by sleeping for a random time between 3 and 10 seconds
        stay_time = random.randint(3, 10)
        time.sleep(stay_time)  # Sleep to simulate eating time
        print(f"{self.name} has finished eating")

# Cafe class: Manages the tables and guest flow in the cafe
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Queue for guests waiting for tables
        self.tables = list(tables)  # Store tables as a list

    def guest_arrival(self, *guests):
        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:  # Check if the table is free
                    table.guest = guest  # Seat the guest at this table
                    guest.start()  # Start the guest thread
                    print(f"{guest.name} sat down at table number {table.number}")
                    seated = True
                    break
            if not seated:
                self.queue.put(guest)  # Add the guest to the queue if no table is free
                print(f"{guest.name} in line")  # Change from 'in queue' to 'in line'

    def discuss_guests(self):
        while True:
            # Check if any guest has finished eating
            active_guests = False
            for table in self.tables:
                if table.guest is not None:
                    active_guests = True  # There's still an active guest
                    if not table.guest.is_alive():  # Check if the guest has finished eating
                        print(f"{table.guest.name} ate and left")  # Changed to 'ate and left'
                        print(f"Table number {table.number} is free")
                        table.guest = None  # Free the table

            # Check if there's a guest in the queue and a free table
            if not self.queue.empty():
                for table in self.tables:
                    if table.guest is None and not self.queue.empty():  # Found a free table
                        next_guest = self.queue.get()  # Get the next guest from the queue
                        table.guest = next_guest  # Seat the guest at the table
                        next_guest.start()  # Start the guest thread
                        print(f"{next_guest.name} left the line and sat down at table number {table.number}")  # Change from 'queue' to 'line'

            # Exit loop if no guests are seated and the queue is empty
            if not active_guests and self.queue.empty():
                break



# Create tables
tables = [Table(number) for number in range(1, 6)]

# Create guests
guest_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
               'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guest_names]

# Fill the cafe with tables
cafe = Cafe(*tables)

# Guests arrive at the cafe
cafe.guest_arrival(*guests)

# Simulate the serving of guests
cafe.discuss_guests()
