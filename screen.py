#!/usr/bin/python

class Screen(object):

    def __init__(self, stdscr, screensaver=True):
        self.stdscr = stdscr
        self.screensaver = screensaver
        self.step = 0

    @property
    def randpos(self):
        from random import randrange as rr
        return (rr(l) for l in self.stdscr.getmaxyx())

    def update(self, clear=False, wait=0):
        if ( self.screensaver and self.stdscr.getch() != -1 ):
            raise KeyboardInterrupt()

        if clear:
            self.stdscr.clear()
        self.stdscr.refresh()

        from time import sleep
        if wait:
            sleep(wait)

    def putstr(self, text, typing=False, delay=0.1):
        if typing:
            for c in text:
                self.stdscr.addstr(c)
                self.update(wait=delay)
        else:
            self.stdscr.addstr(text)
            self.update()

    def put(self, char):
        self.stdscr.addstr(*char.c)