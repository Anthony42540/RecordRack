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
        self.albumReleaseDate = album['release_date']
        self.albumNumTracks = album['total_tracks']
        self.artistName = album['artists'][0]['name']

def mergeSort(array, left, right):
    if (left < right):
        # m is the point where the array is divided into two subarrays
        mid = left + (right - left) / 2
        mergeSort(array, left, mid)
        mergeSort(array, mid + 1, right)
        # Merge the sorted subarrays
        merge(array, left, mid, right)

def merge(array, left, mid, right):
    # Create X ← arr[left..mid] & Y ← arr[mid+1..right]
    n1 = mid - left + 1
    n2 = right - mid
    X = [0] * n1
    Y = [0] * n2
    for i in range(0, n1):
        X[i] = array[left + i]
    for i in range(0, n2):
        Y[i] = array[mid + 1 + i]
    # Merge the arrays X and Y into arr
    i = 0
    j = 0
    k = left
    while (i < n1 and j < n2):
        if X[i] <= Y[j]:
            array[k] = X[i]
            i += 1
        else:
            array[k] = Y[j]
            j += 1
            k += 1
    # When we run out of elements in either X or Y append the remaining elements
    while (i < n1):
        array[k] = X[i]
        i += 1
        k += 1
    while (j < n2):
        array[k] = Y[j]
        j += 1
        k += 1

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
array = []  # initialize empty array that represents the collection

print()
print(">>> Welcome to RecordRack " + displayName + "!")

while True:
    print()
    print("---RecordRack Menu---")
    print("1 - Add to collection")  # all options are to-do
    print("2 - Remove from collection")
    print("3 - View collection")
    print("4 - Sort by album name")
    print("5 - Sort by artist name")
    print("6 - Sort by release date")
    print("7 - Sort by total number of tracks")
    print("X - Exit")
    print()
    choice = input("Your choice: ")
    print()

    if choice == "1":  # add to collection
        searchQuery = input("Ok, what record do you want to add?\n")
        print()
        obj = Album(searchQuery)
        verify = input("You entered: " + obj.albumName + " - " + obj.artistName + "\nIs this the record you were looking for? Yes or no?\n")
        if verify == "Yes" or verify == "yes":
            array.append(obj)  # add the object into the collection
            print()
            print(obj.albumName + " - " + obj.artistName + " has been added to your collection.")
        elif verify == "No" or verify == "no":
            print()
            print("Sorry, try adding more information like the artist name!")
        else:
            print()
            print("That's not a valid answer -_-")
    elif choice == "2":  # remove from collection, for now print() so we don't have errors
        if len(array) != 0:
            recordToDelete = input("What record would you like to remove?\n")
            objToDelete = Album(recordToDelete)
            exist = False
            for i in array:
                if objToDelete.albumName == i.albumName:
                    print()
                    verify = input("Is this the record you want to remove? " + objToDelete.albumName + " - " + objToDelete.artistName + " - Yes or no?\n")
                    if verify == "Yes" or verify == "yes":
                        array.remove(i)  # add the object into the collection
                        print()
                        print(objToDelete.albumName + " - " + objToDelete.artistName + " has been removed from your collection.")
                    elif verify == "No" or verify == "no":
                        print()
                        print("Sorry, try adding more information like the artist name!")
                    else:
                        print()
                        print("That's not a valid answer -_-")
                    exist = True
            if not exist:
                print()
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
    # maybe ask for user input on what sorting method to use?
    elif choice == "4":  # sort by album name
        print()
    elif choice == "5":  # sort by artist name
        print()
    elif choice == "6":  # sort by release date
        print()
    elif choice == "7":  # sort by total number of tracks
        print()
    elif choice == "X" or choice == "x":  # exit the while
        break
    else:
        print("Sorry that's not a valid choice. Try inputting a number 1 - 4 or exit!")

# Prints out a json formatted album, this is just to see what info we can access later
# print(json.dumps(searchResults, sort_keys=True, indent=4))