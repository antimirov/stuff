import os
import sys
import time
import threading


"""
This should be done in multi-threaded way :(
"""


class Shaper:
    def __init__(self, file, speed):
        self.file = file
        self.speed = speed
        self.queue = []
        self.curtime = round(time.time())
        self.curcount = 0

    def read(num=None):
        #while round(time.time()) == self.curtime:
        #while count < num:
        res = self.file.read(num)
        read_bytes = len(res)
        self.count += read_bytes
        if self.count <= self.speed:
            if round(time.time()) == self.curtime:
                return res
        else:
            count = 0
            while 
        



def test_read(fr0m, to, speed):
    s = Shaper(fr0m, speed)
    while True:
        buf = s.read(1024)
        if buf:
            to.write(buf)
        else:
            return




if __name__ == "__main__":
    f = open("from.dat", "r")
    t = open("to.dat", "w")

    test_read(f,t,32*1024)

