import methods
from glob import glob


def main():

    artists = ['The Beatles']

    """ Need to code in a check to look if the file has been moved arleady """

    for artist in artists:

        #artist = 'Bing Crosby'
        
        original_folder_artist_path = f'/Volumes/PAGE 394/Page 394 Library/Media.localized/{artist}'

        artist_folder_path = methods.create_artist_folder_path(artist=artist)
        
        #print(artist_folder_path)
        #print('')

        for album in glob(f'{original_folder_artist_path}/*'):

            album_name = album.split('/')[-1]

            album_folder_path = methods.create_album_folder_path(artist_folder_path,album=album_name)
            #print('*****')
            #print(album_folder_path)
            #print('')

            methods.create_album_folder(folder_path=album_folder_path)

            for file in glob(f'{original_folder_artist_path}/{album_name}/*'):
                
                methods.copy_file(source_file_path=file,destination_folder=album_folder_path)

            
            for file in glob(f'{album_folder_path}/*'):

                methods.rename_file(file)

            



    



if __name__ == "__main__":

    main()