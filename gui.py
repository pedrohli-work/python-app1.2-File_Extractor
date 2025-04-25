import FreeSimpleGUI as sg
from zip_extractor import extract_archive

# Set the theme of the GUI to "LightBlue2"
sg.theme("LightBlue2")

# Creating a label widget for "Select archive:"
label1 = sg.Text("Select archive:")
# Creating an input field where the user can select an archive file
input1 = sg.Input()
#sg.FilesBrowse allow the user to select files on their file system.
choose_button1 = sg.FileBrowse("Choose", key="archive")

# Creating a label widget for "Select directory:"
label2 = sg.Text("Select directory:")
# Creating an input field where 
# the user can specify the destination directory
input2 = sg.Input()
#sg.FolderBrowse allow the user to select folders on their file system.
choose_button2 = sg.FolderBrowse("Choose", key="folder")

# Creating a button labeled "Extract" that 
# will initiate the extraction process when clicked
extract_button = sg.Button("Extract")
# Creating an output label to display messages, 
# with the text color set to green
output_label = sg.Text(key="output", text_color="green")

# Creating three columns to organize the layout:
#   - Column 1 contains the labels (Select archive and Select directory)
#   - Column 2 contains the input fields for the archive path and the destination folder
#   - Column 3 contains the buttons for choosing the archive and folder
col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])

# Creating the main window with 
# the title "File Extractor" and defining the layout
# The layout is a list of lists, 
# with each sublist representing a row of elements in the window 
window = sg.Window("File Extractor",
                   layout=[[col1, col2, col3], [extract_button]])

while True:
    # The window reads the next event and values from the input elements
    event, values = window.read()
    print(event, values)
    # Storing the path of the selected archive and 
    # destination folder from the input fields
    archivepath = values["archive"]
    dest_dir = values["folder"]
    # Calling the custom function 'extract_archive' to 
    # extract the archive to the destination folder
    extract_archive(archivepath, dest_dir)
    # Updating the output label with 
    # the message "Extraction completed!" once the extraction is done
    window["output"].update(value="Extraction completed!")

# Closing the window after the loop ends 
# (which won't happen here since the loop runs indefinitely)
window.close()
