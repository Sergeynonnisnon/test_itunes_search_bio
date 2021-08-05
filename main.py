#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

Part 1

link: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/

Using the itunes open API (link above), you need to implement a script that will return all songs (and information about them) that are included in this album by the parameters "artist" + "song title".

Input format: any (config file, inside a script, input(), cli)
Output format: .csv file (see attachment)


Part 2

Using the parameters from the previous part ("artist" + "song title"), find the page with the chords of the song (take the first result from the search results), parse the text + chords and save them to a .txt file

If there are no results, leave the final file empty.

Input format: any (config file, inside a script, input(), cli)
Output format: .txt file

"""

from settings import input_song, input_artist
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS


def first_part(input_song, input_artist):
    """first part of task """
    BASE_URL = 'https://itunes.apple.com/search?'
    term = input_artist.replace(' ', '+') + '+' + input_song.replace(' ', '+')

    response = requests.get(BASE_URL + 'term' + '=' + term + '&entity=song').json()
    search_result = response['results']
    print(f'count {len(response["results"])} results')

    albums = {}
    #######
    # get name albums +author
    #######

    for track in search_result:

        if input_song.lower() in str(track['trackName']).lower() \
                and input_artist.lower() in str(track['artistName']).lower():

            albums[track['artistName'] + '+' + str(track['collectionName']).replace(' ','+')] = track['collectionId']

            print(f'count albums with song is {len(albums)}')
            artist_id=track['artistId']

    #######
    # get song from albums
    #######
    result = []

    for album in albums.keys():
        response = requests.get(BASE_URL + 'term' + '=' + album + '&entity=song')

        response.encoding = response.apparent_encoding
        json_resp = response.json()
        json_resp = json_resp['results']
        #check if album and artist correct
        for i in json_resp:
            if i['artistId'] != artist_id or i['collectionId'] not in albums.values():
                json_resp.remove(i)

        result += json_resp


    print(f'count {len(result)} tracks')

    df = pd.DataFrame(result)
    df.to_csv(f'{input_artist}_track_{input_song}.csv')


#####################################################


def second_part(input_song, input_artist):
    """second part of task """
    response = requests.get('https://searx.roughs.ru/search',
                            params={'q': f'{input_song} - {input_artist} lyrics  chords', 'format': 'json',
                                    'safesearch': 1})

    print(f" first entry link{response.json()['results'][0]['pretty_url']}")
    try:
        lyrics_chords = requests.get(response.json()['results'][0]['pretty_url'])
        soup = BS(lyrics_chords.content, 'lxml', ).body.get_text()

        with open(f'text_{input_artist}_{input_song}.txt', 'w', encoding='utf-8') as f:
            f.write(soup)


    except IndexError:
        with open(f'text_{input_artist}_{input_song}.txt', 'w') as f:
            pass


if __name__ == '__main__':
    first_part(input_song, input_artist)
    second_part(input_song, input_artist)
