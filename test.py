import re

fileName = input("Enter the file name: ")
total = 0
try:
    with open(fileName, 'r') as file:
        for lines in file:
            numbers = re.findall('[0-9]+', lines)
            total += sum(int(num) for num in numbers)
    print(f"The total sum is: {total}")

except FileNotFoundError:
    print(f"Error: The file '{fileName}' was not found.")

