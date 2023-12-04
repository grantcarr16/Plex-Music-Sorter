from methods import rename_file
from glob import glob

artist = 'Curren$y'
album = r"Canal Street Confidential"

def double_backslash_remover(path_list)->list:
    
    path_list = [path.replace('\\','/') for path in path_list]

    return path_list

file_path = f'C:/Users/grant/Desktop/Music/Plexamp/{artist}/{album}/*'

for file in double_backslash_remover(glob(file_path)):
    rename_file(file_path=file)