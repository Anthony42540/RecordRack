# RecordRack

RecordRack is an application where you can store your collection of records.

## Installation

1. Install Spotipy by opening the terminal and run this command:

```bash
python3 -m pip install spotipy
```

2. Now we need to set variables in the terminal from the app we create on https://developer.spotify.com/dashboard/

On Windows: 
```bash
$env:SPOTIPY_CLIENT_ID="XXXX"
```
```bash 
$env:SPOTIPY_CLIENT_SECRET="XXXX"
```
```bash
$env:SPOTIPY_REDIRECT_URI="http://google.com/"
```

On Mac: 
```bash
export SPOTIPY_CLIENT_ID='XXXX'
```
```bash 
export SPOTIPY_CLIENT_SECRET='XXXX'
```
```bash
export SPOTIPY_REDIRECT_URI='XXXX'
```
I think that's it

## Running

1. Run this command 
```bash
python3 "name-of-your-.py-file" "username"
```
* You can get your username from the URL when you click "Copy Profile Link", it should be after "user/" and isn't always your actual username (might be an ID)

