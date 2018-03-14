#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
S2L Sound to Letter tool

Tool that will canverts sounds to letters 
"""

import sys
import urwid
import wave
import struct
import time

__author__ = "Paweł Siergiejuk"
__date__ = "14/03/2018"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


class Application:
    WV_FILE = "res/test.wv"    

    def __init__(self):
       pass


    def main(self):
        bar = urwid.BarGraph(['normal', 'inverse'],
         ['normal', 'inverse'],
         { (1,0): 'normal', })
        track = wave.open(self.WV_FILE, "r")
        self.length = track.getnframes()
        data = []
        self.count = 0
        sample = track.getsampwidth()
        def tic(_loop, _data):
            if self.count > self.length:
                urwid.ExitMainLoop()
            else:
                wv_data = track.readframes(1)
                data.append(struct.unpack("<h", wv_data))
                if self.count > 100:
                    data.pop(0)
                bar.set_data(data,100)
                self.count += 1
                win.set_alarm_in(0.01, tic)

    
        def next_data(key):
            if key == "q":
                urwid.ExitMainLoop()
                
        win = urwid.MainLoop(bar, unhandled_input=next_data)
        win.set_alarm_in(0, tic)
        win.run()
        """
        for i in range(0,length):
            wv_data = track.readframes(1)
            sample = track.getsampwidth()
            data = struct.unpack("<h", wv_data)[0]
            int_data = int(data/100)
            if data > 0:
                out = " "*60 + "#"*(int_data)
            else:
                out = " "*(60 + int_data) + "#"*(abs(int_data))
            print(sample*i, out)
            time.sleep(0.0001)
        """

if __name__ == "__main__":
    app = Application()
    app.main()


