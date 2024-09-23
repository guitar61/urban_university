# Importing necessary libraries
import pandas as pd
import numpy as np
from PIL import Image, ImageFilter


# 1. pandas - Reading a CSV file, analyzing, and outputting results
def pandas_analysis():
    # Load a CSV file
    data = pd.read_csv('sample_data.csv')  # Ensure you have 'sample_data.csv'

    # Display basic statistics of the data
    print("Basic statistics of the dataset:")
    print(data.describe())  # Displays count, mean, std, min, max, and percentiles for numeric columns

    # Filter the data: Select rows where 'Age' is greater than 25
    filtered_data = data[data['Age'] > 25]
    print("\nFiltered data (Age > 25):")
    print(filtered_data)

    # Group by 'Department' column and calculate the mean 'Salary'
    salary_mean = data.groupby('Department')['Salary'].mean()
    print("\nAverage salary by department:")
    print(salary_mean)


# 2. numpy - Creating an array, performing operations, and outputting results
def numpy_operations():
    # Create a NumPy array
    array = np.array([1, 2, 3, 4, 5])

    # Perform mathematical operations
    array_sum = np.sum(array)
    array_mean = np.mean(array)
    array_square = np.square(array)

    # Output the results
    print("\nNumpy Array: ", array)
    print(f"Sum of array: {array_sum}")
    print(f"Mean of array: {array_mean}")
    print(f"Square of each element: {array_square}")


# 3. Pillow - Image processing (resizing, applying filters, and saving)
def process_image():
    # Load an image from file
    img = Image.open('sample_image.jpg')  # Make sure you have an image named 'sample_image.jpg'

    # Resize the image
    resized_img = img.resize((300, 300))  # Resize the image to 300x300 pixels
    resized_img.show()  # This will display the resized image

    # Apply a blur filter to the image
    blurred_img = resized_img.filter(ImageFilter.BLUR)  # Apply a blur effect
    blurred_img.show()  # This will display the blurred image

    # Save the modified image in a different format
    blurred_img.save('blurred_image.png', 'PNG')  # Save the new image as a PNG file
    print("Image saved as 'blurred_image.png'")


# Running all functions
if __name__ == "__main__":
    print("Pandas Analysis:")
    pandas_analysis()  # Perform pandas operations

    print("\nNumpy Operations:")
    numpy_operations()  # Perform numpy operations

    print("\nPillow Image Processing:")
    process_image()  # Perform image processing
