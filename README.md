File Analyzer CLI Tool

A small Python command-line program to analyze files in a folder.

It helps you:

Group files by size
Find possible duplicates (based on file size)
Search files by name
Search files by extension
Count total files in a folder

How to Use
Make sure Python 3 is installed.
Download or clone this project.
Open a terminal in the project folder.

Run the program:
python main.py

Enter the folder path you want to analyze.
Use the menu to choose an action.

Example Menu

--- File Analyzer Menu ---
1. Group files by size
2. Show possible duplicate files
3. Search file by name
4. Search files by extension
5. Number of files found
6. Exit
   
Notes
Only top-level files are analyzed; subfolders are ignored.
Duplicate detection is based on file size only.
File searches are case-insensitive.

Future Ideas
Detect exact duplicates using file hashes.
Include subfolders in the scan.
Add move/copy tools to organize files automatically.
Sort files by size or name in outputs.
