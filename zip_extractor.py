"""
This module provides a function to extract the contents of a ZIP archive.

It uses the Python built-in 'zipfile' module to handle ZIP file extraction.
The main function, `extract_archive`, takes the path to a ZIP file and a destination directory,
then extracts all files from the archive to the specified location.

Usage:
    If this module is run directly, it will extract a sample ZIP file ("compressed.zip")
    to the destination directory ("Users/files").

Dependencies:
    - zipfile (Python Standard Library)
"""

import zipfile

# Defining a function named 'extract_archive' that takes two arguments:
#   - 'archivepath': the path to the ZIP file
#   - 'dest_dir': the destination directory where 
# the contents of the archive will be extracted
def extract_archive(archivepath, dest_dir):
    """
    Extracts the contents of a ZIP archive to the specified directory.

    Parameters:
    archivepath (str): The path to the ZIP file to be extracted.
    dest_dir (str): The destination directory where the contents of the archive will be extracted.
    
    The function opens the ZIP file, extracts all its contents, and saves them to the destination directory.
    """
    # Using the 'with' statement to open the ZIP file in read mode ('r')
    # The 'with' statement ensures that the file 
    # is properly closed after the block of code is executed
    with zipfile.ZipFile(archivepath, 'r') as archive:
        # Extracting all the contents of 
        # the ZIP archive to the specified destination directory
        # 'extractall()' extracts all files in 
        # the archive to the destination directory
        archive.extractall(dest_dir)

# Checking if this script is being run directly
if __name__ == "__main__":
    # If the script is being run directly, 
    # calling the 'extract_archive' function
    # with a sample ZIP file ("compressed.zip") 
    # and the target extraction directory ("Users/files")
    extract_archive("compressed.zip", "Users/files")
