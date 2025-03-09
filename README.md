# Folder and Random Numbers Generator

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Example](#example)
7. [License](#license)

## Overview
This Python script allows users to create a folder and generate a file containing 99 random numbers ranging from 1 to 1000. It demonstrates basic file and folder operations using Python's built-in `os` and `random` libraries.

## Features
- Creates a folder if it does not already exist.
- Generates 99 random numbers and stores them in a text file.
- Reads and prints the contents of the generated file to the terminal.
- Uses Python standard libraries (`os` and `random`).

## How It Works
1. The script prompts the user to enter a folder name.
2. It checks if the folder exists:
   - If not, it creates the folder.
3. Generates 99 random integers ranging from 1 to 1000.
4. Writes the list of numbers to a file named `numbers100.txt` inside the created folder.
5. Opens and prints the contents of `numbers100.txt` to the terminal.

## Installation
No installation is required for this script.
Make sure you have Python 3 installed on your system.

## Usage
1. Open your terminal or command prompt.
2. Run the script:

```bash
python3 folders-and-files.py
```

3. Follow the prompt to enter a folder name.
4. The program will create the folder, generate the file, and display its contents.

## Example
```
Please enter your folder name
example_folder
[168, 999, 245, 782, 543, ..., 456]
```

## License
This project is for educational purposes. No additional licensing terms apply.
