import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

class Album:
    def __init__(self, albumObj):
        # Gets the search results based on what album name the user inputs
        searchResults = spotifyObject.search(albumObj, 1, 0, "album")
        # Get the album details
        album = searchResults['albums']['items'][0]
        self.albumName = album['name']
        self.artistName = album['artists'][0]['name']

# Get the username from the terminal
username = sys.argv[1]

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
array = []  # initialize empty array that represents the collection

print()
print(">>> Welcome to RecordRack " + displayName + "!")

while True:
    print()
    print("---RecordRack Menu---")
    print("1 - Add to collection")  # all options are to-do
    print("2 - Remove from collection")
    print("3 - View collection")
    print("4 - Different sort options")
    print("X - Exit")
    print()
    choice = input("Your choice: ")
    print()

    if choice == "1":  # add to collection
        searchQuery = input("Ok, what record do you want to add?: ")
        print()
        obj = Album(searchQuery)
        verify = input("You entered: " + obj.albumName + " - " + obj.artistName + "\nIs this the record you were looking for? Yes or no?\n")
        if verify == "Yes" or verify == "yes":
            array.append(obj)  # add the object into the collection
        else:
            print()
            print("Sorry, try adding more information like the artist name!")
    elif choice == "2":  # remove from collection, for now print() so we don't have errors
        if len(array) != 0:
            recordToDelete = input("What record would you like to remove?\n")
            exist = False
            for i in array:
                if recordToDelete == i.albumName:
                    albumObjToDelete = i
                    exists = True
            if exists:
                array.remove(albumObjToDelete)
                print()
                print(albumObjToDelete.albumName + " has been removed.")
            else:
                print("This record isn't in your collection!")
        else:
            print("You don't have any records to remove!")


    elif choice == "3":  # view collection
        if len(array) != 0:
            print("---Your collection---")
            for i in array:
                print(i.albumName + " - " + i.artistName)
        else:
            print("You don't have any records in your collection!")
    elif choice == "4":  # different sort options, for now print() so we don't have errors
        print()
    elif choice == "X":  # exit the while
        break

# Prints out a json formatted album, this is just to see what info we can access later
# print(json.dumps(searchResults, sort_keys=True, indent=4))