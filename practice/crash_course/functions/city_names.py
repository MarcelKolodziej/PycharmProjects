# def city_country_names(city, country):
#     "Return neatly formatted city with country"
#     formatted_city_country = print(f"Welcome in {city}, {country}")
#
# city_country_names('Santaigo', 'Bernabeu')
# city_country_names('Warsaw', 'Poland')
# city_country_names('Santiago', 'Chile')

def make_album(artist_name, album_title, number_of_songs=None):
    """Return dictionary"""
    album = {'artist name': artist_name, 'album_title': album_title, 'number_of_songs':number_of_songs }
    if number_of_songs:
        album['number_of_songs'] = number_of_songs

    else:
        album = (f"{artist_name} {album_title}")
        return album


print(make_album('Jimmy Hendrix', 'Stair Way to Heaven'))
print(make_album('Jimmy Hendrix', 'Stair Way to Heaven', 12))
