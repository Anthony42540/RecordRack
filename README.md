# RecordRack

RecordRack is an application where you can store your collection of records/vinyls using the Spotify API.

## Installation

1. Install Spotipy by opening the terminal and run this command:

```bash
python3 -m pip install spotipy
```

2. Now we need to set variables in the terminal (Windows Powershell or Mac Terminal) from the app we create on https://developer.spotify.com/dashboard/.

    a. Login to the Spotify developer site with your usual Spotify credentials (free or premium accounts), or make an account.

    b. Create an app on the dashboard page. Fill out the app name and app description with whatever you prefer, and the redirect URI should be "http://google.com/".

    c. After creating your app, click on the app from your dashboard and go to settings. There you can access your client ID and secret. Now use these values in the following terminal commands to save them for later use in the program.

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
export SPOTIPY_REDIRECT_URI='http://google.com/'
```
Now you're ready to run the program!
## How to run
1. Run this command in the terminal (Windows Powershell or Mac Terminal)
```bash
python3 RecordRack.py <username>
```
Example: "python3 RecordRack.py nightwing42540"

You can get your username from the URL when you click "Copy Profile Link", it should be after "user/" and before the "?". This isn't always your actual username (might be an ID).



