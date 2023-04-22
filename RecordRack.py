import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from the terminal
username = sys.argv[1]

# User ID: nightwing42540

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']

while True:

    print()
    print(">>> Welcome to RecordRack " + displayName + "!")
    print()
    print("1 - Add to collection") # all options are to-do
    print("2 - Remove from collection")
    print("3 - View collection")
    print("4 - Different sort options")
    print("X - Exit")
    print()
    choice = input("Your choice: ")

    if choice == "1":  # add to collection
        print()
        searchQuery = input("Ok, what record do you want to add?: ")
        print()
        searchResults = spotifyObject.search(searchQuery, 1, 0, "album")  # gets the search results based on what album name the user inputs
        print(json.dumps(searchResults, sort_keys=True, indent=4))  # prints out a json formatted album, this is just to see what info we can access later
    if choice == "2":  # remove from collection, for now print() so we don't have errors
        print()
    if choice == "3":  # view collection, for now print() so we don't have errors
        print()
    if choice == "4":  # different sort options, for now print() so we don't have errors
        print()
    if choice == "X":  # exit the while
        break

