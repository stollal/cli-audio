import curses
import curses.textpad
import sys
from exception_handling import handle as ha

class FrontEnd:

    def __init__(self, player):
        self.player = player
        self.player.play(sys.argv[1])
        curses.wrapper(self.menu)

    def menu(self, args):
        self.stdscr = curses.initscr()
        if self.stdscr.getmaxyx()[0] < 25 or self.stdscr.getmaxyx()[1] < 80:
            raise ha.CLI_Audio_Screen_Size_Exception('Screen size is too small: Minimum width is 80, and minimum length is 25')
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                self.musicLibrary()
    
    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())
        self.stdscr.addstr(17,10, "Up Next: " ) ## + self.player.getNextSong())

    def changeSong(self):
        changeWindow = curses.newwin(5, 40, 5, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "What is the file path?", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 30)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()
        self.player.play(path.decode(encoding="utf-8"))

   #Where you can enter your paths and they will go into the queue to create the playlist 
    def musicLibrary(self):
        changeWindow = curses.newwin(25, 40, 25, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "Music Library",curses.A_REVERSE)
        changeWindow.addstr(2,0, "To add music to playlist just enter path and hit enter.",curses.A_REVERSE)
        changeWindow.addstr(3,0, "Create Playlist",curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(4,1, 30)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()
        self.player.play(path.decode(encoding="utf-8"))

    def quit(self):
        self.player.stop()
        exit()
