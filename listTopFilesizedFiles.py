import os

# ask user for device id and number of files to list
while True:
    device_id = input("Enter the device id (e.g. C:): ")
    if os.path.isdir(device_id):
        break
    print("Invalid device id. Please enter a valid device id.")

while True:
    num_files_str = input("Enter the number of files to list: ")
    if not num_files_str.isdigit():
        print("Invalid input. Please enter a positive integer.")
        continue
    num_files = int(num_files_str)
    if num_files > 0:
        break
    print("Invalid input. Please enter a positive integer.")

# get list of files on device and sort by size
file_list = []
for root, dirs, files in os.walk(device_id):
    for name in files:
        try:
            file_size = os.path.getsize(os.path.join(root, name))
            file_list.append((os.path.join(root, name), file_size))
        except:
            # ignore file if it cannot be accessed
            pass
file_list.sort(key=lambda x: x[1], reverse=True)

# print top n files and ask user to select a file to open
while True:
    print("\nSelect a file to open:")
    for i in range(num_files):
        if i >= len(file_list):
            break
        file_path = file_list[i][0]
        file_size = file_list[i][1]
        print(f"{i+1}. {file_path} ({file_size} bytes)")
    print("0. Exit")

    # ask user to enter the index of the file to open
    while True:
        file_index_str = input("Enter the index of the file to open: ")
        if not file_index_str.isdigit():
            print("Invalid input. Please enter a positive integer.")
            continue
        file_index = int(file_index_str)
        if 0 <= file_index <= num_files:
            break
        print(f"Invalid input. Please enter a number between 0 and {num_files}.")

    # exit if user enters 0
    if file_index == 0:
        break

    # open explorer window for the selected file
    file_path = file_list[file_index-1][0]
    os.startfile(os.path.dirname(file_path))
