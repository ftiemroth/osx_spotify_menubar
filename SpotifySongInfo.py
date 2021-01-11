import os
import rumps
import osascript

class spotifyApp(rumps.App):
    def __init__(self):
        super(spotifyApp, self).__init__('IDLE')
        #self.icon = 'logo.png'
    @rumps.timer(1)
    def get_song(self, _):
        artist_title = os.popen('osascript /Applications/SpotifySongInfo.app/current_song_name.scpt').read().strip()
        self.title = artist_title
    @rumps.clicked("Play/Pause")
    def playpause(self, _):
        osascript.run('''
                      tell application "Spotify"
                      playpause
                      end tell
                      ''')
        #os.popen('osascript scripts/playpause.scpt')
    @rumps.clicked('Next')
    def next_song(self, _):
        osascript.run('''
                      tell application "Spotify"
                      next track
                      end tell
                      ''')
        #os.popen('osascript scripts/next.scpt')
    @rumps.clicked('Previous')
    def previous_song(self, _):
        osascript.run('''
                      tell application "Spotify"
                      previous track
                      end tell
                      ''')
        #os.popen('osascript scripts/previous.scpt')

if __name__ == "__main__":
    spotifyApp().run()
