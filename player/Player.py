"""PyAudio Example: Play a wave file (callback version)."""

import pyaudio
import wave
import time
import os
from exceptions import Exceptions as ex

class Player:
    def __init__(self):
        self.currentSong = "Nothing playing."
        self.paused = True
        self.position = 0

    def getCurrentSong(self):
        return self.currentSong

    def pause(self):
        if self.paused == False:
            self.paused = True
            self.stream.stop_stream()
        else:
            self.paused = False
            self.stream.start_stream()

    def play(self, track):
        self.paused = False
        self.currentSong = track
        if os.path.isfile(track):
            self.wf = wave.open(track, 'rb')
        else:
            raise ex.CLI_Audio_File_Exception('File not found')

        # instantiate PyAudio (1)
        self.p = pyaudio.PyAudio()

        # open self.stream using callback (3)
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                channels=self.wf.getnchannels(),
                rate=self.wf.getframerate(),
                output=True,
                stream_callback=self.callback)

        # start the self.stream (4)
        self.stream.start_stream()

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()

        self.p.terminate() 

    def callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

# Returns the song that is up next
    def getNextSong(self):
        return self.nextSong

# Song Queue puts the paths entered in a queue and continuously plays through them until reaches end
    def songQueue(self, track):
        if self.pause == False:
            self.wf = wave.open(track, 'rb')
            
