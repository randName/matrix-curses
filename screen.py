#!/usr/bin/python

import curses

class Screen(object):

    def __init__(self, stdscr, screensaver=True):
        curses.curs_set(0)
        curses.init_pair(1, 34, 18)
        curses.init_pair(2, 82, 18)

        stdscr.nodelay(1)
        stdscr.scrollok(False)
        stdscr.bkgd(' ',curses.color_pair(1))

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
        if clear: self.stdscr.clear()
        self.stdscr.refresh()
        from time import sleep
        if wait: sleep(wait)

    def putstr(self, text, typing=False, delay=0.1):
        if typing:
            for c in text:
                self.stdscr.addstr(c)
                self.update(wait=delay)
        else:
            self.stdscr.addstr(text)
            self.update()

    def put(self, char):
        try:
            self.stdscr.addstr(*char.c)
        except curses.error:
            char.update(reset=True)