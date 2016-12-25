#!/usr/bin/python

from curses import wrapper
from screen import Screen
from character import RainChar, BlankChar

def main(scr, rain_chars=50, blank_chars=100):

    breaks = "\n" * 4

    opening = breaks.join((
        "Wake Up, Neo...",
        "The Matrix has you...",
        "Follow the white rabbit..."
    ))

    closing = breaks + "Knock, Knock, Neo..." + breaks

    s = Screen(scr)
    RainChar.setscreen(s)
    BlankChar.setscreen(s)
    chars = RainChar.get(rain_chars) + BlankChar.get(blank_chars)

    s.putstr(opening, typing=True)
    s.update(clear=True)

    try:
        while True:
            s.update(wait=1.0/25)
            s.step += 1
            for c in chars: c.update()
    except KeyboardInterrupt:
        s.update(clear=True)
        s.putstr(opening)
        s.putstr(closing, typing=True)

wrapper(main)
