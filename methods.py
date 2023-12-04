import os
import shutil
from glob import glob


def create_artist_folder_path(artist,path) -> str:

    folder_path = f'{path}/{artist}'

    return folder_path


def create_album_folder_path(artist_path,album) -> str:

    folder_path = f'{artist_path}/{album}'

    return folder_path


def create_album_folder(folder_path) -> None:
    
    # Check if the folder exists
    if not os.path.exists(folder_path):
        # Create the folder
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")


def copy_file(source_file_path, destination_folder) -> None:

    # Check if the source file exists
    if not os.path.exists(source_file_path):
        print(f"Source file '{source_file_path}' does not exist.")
        return
    
    #This section doesn't work in Windows??
    # Check if the destination folder exists
    #if not os.path.exists(destination_folder):   
    #    os.makedirs(destination_folder)
    #    #print(f"Created {destination_folder}")
    #else:
    #    #print(f"Destination folder {destination_folder} already exists")
    #    return
    
    # Get the file name from the source path
    file_name = os.path.basename(source_file_path)
    #print(file_name)

    if not os.path.exists(os.path.join(destination_folder, file_name)):    
        # Create the destination file path
        destination_file_path = os.path.join(destination_folder, file_name)
    else:
        print(f'{file_name} already exists in {destination_folder}')

    
    # Copy the file
    shutil.copy(source_file_path, destination_file_path)
    #print(f"File '{file_name}' copied to '{destination_folder}'.")


def rename_file(file_path) -> None:
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return
    
    # Get the file name and extension
    file_name = os.path.basename(file_path)
    name, ext = os.path.splitext(file_name)
    
    # Check if the file follows the naming convention
    parts = name.split(" ", 1)
    if len(parts) == 2 and parts[0].isdigit():
        new_name = f"{parts[0]} - {parts[1]}{ext}"
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        
        # Rename the file
        os.rename(file_path, new_path)
        #print(f"Renamed '{file_name}' to '{new_name}'.")
    else:
        print(f"File '{file_name}' does not follow the expected naming convention.")
