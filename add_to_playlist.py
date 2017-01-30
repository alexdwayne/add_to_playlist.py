import os
os.environ["SPOTIPY_CLIENT_ID"] = "bba9f428ab554d2cb3c18ed1f452c698"
os.environ["SPOTIPY_CLIENT_SECRET"]= 'c6f2262eb935415b95a1591c8cb96479'
os.environ["SPOTIPY_REDIRECT_URI"]= 'http://alexdwayne.com'


import pprint
import sys

import spotipy
import spotipy.util as util

import csv

username = sys.argv[1]
playlist_id = sys.argv[2]


'''
if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    track_ids = sys.argv[3:]
    

else:
    print "Usage: %s username playlist_id track_id ..." % (sys.argv[0],)
    sys.exit()

'''

scope = 'playlist-modify-private'
token = util.prompt_for_user_token(username, scope)


csvreader = csv.reader(open("collections_ids_csv.csv"), delimiter=",")

for line in csvreader:
    try:

        track_ids= line

        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        print results

    except:

        continue 


