import methods
from glob import glob

def double_backslash_remover(path_list)->list:
    
    path_list = [path.replace('\\','/') for path in path_list]

    return path_list



def main():



    #itunes_path = 'C:/Users/grant/Desktop/Music/Itunes Library/Music'
    itunes_path = 'C:/Users/grant/Music/iTunes/iTunes Media/Music'
    plexamp_path = 'C:/Users/grant/Desktop/Music/Plexamp'

    artists = []
    for folder in double_backslash_remover(glob(f'{itunes_path}/*')):
        artist = folder.split('/')[-1]
        artists.append(artist)

    print(artists)


    for artist in artists:

        #artist = 'Bing Crosby'
        
        original_folder_artist_path = f'{itunes_path}/{artist}'
        #print(original_folder_artist_path)
        artist_folder_path = methods.create_artist_folder_path(artist=artist, path=plexamp_path)
        #print(original_folder_artist_path)
        
        album_list = double_backslash_remover(glob(f'{original_folder_artist_path}/*'))
        
        for album in album_list:
            
            album_name = album.split('/')[-1]
            album_folder_path = methods.create_album_folder_path(artist_folder_path,album=album_name)
            methods.create_album_folder(folder_path=album_folder_path)
            album_file_list = double_backslash_remover(glob(f'{original_folder_artist_path}/{album_name}/*'))

            for file in album_file_list:
                #print(file)
                #print(album_folder_path)
                methods.copy_file(source_file_path=file,destination_folder=album_folder_path)

            plex_album_file_list = double_backslash_remover(glob(f'{album_folder_path}/*'))
            
            for file in plex_album_file_list:

                methods.rename_file(file)

            



    



if __name__ == "__main__":

    main()