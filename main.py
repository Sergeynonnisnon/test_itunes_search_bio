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
import pandas

from settings import input_song, input_artist
import itunespy
import pandas as pd
import csv
import json

def first_part(input_song,input_artist):
    tracks = itunespy.search_track(input_song)

    received_tracks = []
    for artist in tracks:
        if artist.artist_name == input_artist:
            albums = itunespy.search_album(artist.collection_name)
            frames = []
            for album in albums:
                if album.artist_name == input_artist:
                    list_traks = []
                    for i in album.get_tracks():
                        list_traks.append(i.json)
                    df = pandas.DataFrame(list_traks)
                    df.to_csv(f'{input_artist}_tracks.csv')

        break


import requests
import 
def second_part(input_song,input_artist):

