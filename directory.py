import os
import time

# Start in the current directory
directory = "."

for root, dirs, files in os.walk(directory):
    for file in files:
        # 1. Form the full path to the file
        filepath = os.path.join(root, file)

        # 2. Get the last modification time of the file
        filetime = os.path.getmtime(filepath)

        # 3. Format the modification time
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # 4. Get the size of the file
        filesize = os.path.getsize(filepath)

        # 5. Get the parent directory
        parent_dir = os.path.basename(root)

        # Print the file details
        print(
            f'File found: {file}, Path: {filepath}, Size: {filesize} bytes, Modified time: {formatted_time}, Parent directory: {parent_dir}')
