# week4.py-assignment
Line numbering tool assignment
📄 Line Numbering Tool
📌 Overview

The Line Numbering Tool is a simple Python program that reads the contents of a text file, adds line numbers to each line, and saves the modified content into a new file.

It demonstrates practical file handling and error handling in Python, ensuring the program runs smoothly even if the file doesn’t exist or access is restricted.

🚀 Features

Reads any text file line by line.

Adds line numbers in the format:

1: First line
2: Second line
3: Third line


Saves the modified content into a new file prefixed with numbered_.

Handles common errors gracefully:

Missing file (FileNotFoundError)

Permission denied (PermissionError)

Unexpected issues (generic Exception)

🛠️ Requirements

Python 3.x installed on your system.

A text file (e.g., notes.txt) to test with.

📂 Usage

Save the script as line_numbering.py.

Place it in the same directory as the file you want to process (or provide a full path).

Run the program from the terminal or command prompt:

python line_numbering.py


Enter the filename when prompted:

📂 Enter the filename to read: notes.txt


The program will generate a new file named:

numbered_notes.txt

🔎 Example

Input file (notes.txt):

Python is fun
File handling is powerful
Error handling makes code robust


Output file (numbered_notes.txt):

1: Python is fun
2: File handling is powerful
3: Error handling makes code robust

⚠️ Error Handling

If the file does not exist:

❌ Error: The file 'notes.txt' does not exist.


If access is denied:

❌ Error: You don’t have permission to read 'notes.txt'.


If another error occurs:

⚠️ An unexpected error occurred: <error details>
