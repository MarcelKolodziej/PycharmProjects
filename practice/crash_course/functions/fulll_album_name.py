def full_album_name(artist_name, song_name):
    """Return neatly formatted full artist and album name"""
    full_name = {'artist name': artist_name, 'song_name': song_name}
    return full_name


while True:
    print("type 'q' for quit the program")
    print("Tell me artist name and song name")

    artist_name = input("artist name: ")
    if artist_name == 'q':
        break

    song_name = input("Tell me song name: ")
    if song_name == 'q':
        break

    formatted_name = full_album_name(artist_name, song_name)
    print(f"\n{formatted_name}")
