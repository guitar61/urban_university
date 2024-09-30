import time
import multiprocessing


# Function to read data from a file line by line
def read_info(name):
    all_data = []  # List to store all lines from the file
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Stop when we reach the end of the file
                break
            all_data.append(line)


# Sequential execution (linear approach)
def sequential_execution():
    filenames = [f'./file{number}.txt' for number in range(1, 5)]  # List of 4 files

    start_time = time.time()  # Record the start time

    for name in filenames:  # Sequentially read each file
        read_info(name)

    end_time = time.time()  # Record the end time
    total_time = end_time - start_time  # Calculate the total time

    print(f"Sequential Execution Time: {total_time:.6f} seconds")


# Multiprocessing execution (parallel approach)
def multiprocessing_execution():
    filenames = [f'./file{number}.txt' for number in range(1, 5)]  # List of 4 files

    start_time = time.time()  # Record the start time

    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)  # Use pool to apply read_info concurrently to each file

    end_time = time.time()  # Record the end time
    total_time = end_time - start_time  # Calculate the total time

    print(f"Multiprocessing Execution Time: {total_time:.6f} seconds")


# Main block to run the tests
if __name__ == "__main__":
    # Uncomment one of the following to test either method:

    # Sequential execution
    sequential_execution()

    # Multiprocessing execution
    multiprocessing_execution()
