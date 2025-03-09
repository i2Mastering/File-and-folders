'''
Ike Iloegbu CSC 6303
OS: MacOS 15.0.1 (24A348)
'''

import os
import random

def fileCreate(folderName):
    '''
    Creates a folder (if it does not exist) and generates a text file containing 99 random numbers.
    
    The function performs the following tasks:
    1. Checks if the folder exists; if not, creates it.
    2. Generates 99 random numbers between 1 and 1000.
    3. Writes the list of numbers to a file named 'numbers100.txt' within the folder.
    4. Reads and prints the contents of the file to the terminal.

    Args:
        folderName (str): The name of the folder to create or use for file storage.
    '''

    # Check if the folder exists; create it if it doesn't
    if not os.path.exists(folderName):
        os.makedirs(folderName)

    # Initialize a list to hold 99 random numbers
    numbers = []
    for i in range(1, 100):
        numbers.append(random.randint(1, 1000))

    # Define the file path for numbers100.txt
    file_path = os.path.join(folderName, "numbers100.txt")

    # Write the list of numbers to the file
    with open(file_path, "w") as f:
        f.write(str(numbers))

    # Open the file and print its contents
    with open(file_path, "r") as o:
        print(o.read())

def main():
    '''
    Main function that prompts the user to enter a folder name and calls fileCreate().
    '''
    print('Please enter your folder name')
    folderName = input()
    fileCreate(folderName)

if __name__ == "__main__":
    main()
