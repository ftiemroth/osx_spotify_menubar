# osx_spotify_menubar

## About
Rumps based app to display the current song from Spotify on the menu bar. 

You can also play/pause and change to next/previous track.

## Demo
![demo](https://github.com/ftiemroth/osx_spotify_menubar/blob/main/demo/demo.gif?raw=true)

## Compatibilty
Tested on macOS Catalina (10.15.7)

Not tested on older versions yet (pending)

## Easy install
Download the file [SpotifySongInfo.zip](https://github.com/ftiemroth/osx_spotify_menubar/blob/main/SpotifySongInfo.zip) and move SpotifySongInfo.app to your `Applications` folder.

Since I don't have an Apple developer account you will receive an 'Unknonwn Developer' warning. This can be bypassed by using right click > 'Open'. You can find more info [here](https://support.apple.com/kb/PH25088?locale=en_US).

## Dependencies
`rumps`

`osascript`

## Build
You can build the app yourself using pyinstaller and the following command:

`pyinstaller --clean --onefile --noconsole SpotifySongInfo.py`

This will create a folder `dist` with a .app file, you should right click > 'Show package contents' and copy the file 'current_song_name.scpt' (found on the scripts folder)
