from methods import rename_file
from glob import glob

artist = 'The Beatles'
album = "The Beatles"

file_path = f'/Users/grantcarr/Desktop/Plex Music/{artist}/{album}/*'

for file in glob(file_path):
    rename_file(file_path=file)