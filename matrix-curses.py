#!/usr/bin/python

import curses
from screen import Screen
from character import RainChar, BlankChar

def main(scr, rain_chars=50, blank_chars=100):

    colors = ((1, 34, 232), (2, 82, 232))

    prompt_text = (
        "Wake up, Neo...",
        "The Matrix has you...",
        "Follow the white rabbit.",
        "Knock, knock, Neo."
    )

    scr.nodelay(1)
    scr.scrollok(False)
    scr.bkgd(' ', curses.color_pair(1))
    for c in colors:
        curses.init_pair(*c)
    curses.curs_set(0)

    s = Screen(scr)
    RainChar.setscreen(s)
    BlankChar.setscreen(s)
    chars = RainChar.get(rain_chars) + BlankChar.get(blank_chars)

    for line in prompt_text[:-1]:
        s.putstr(line + "  ", typing=True)
        s.update(clear=True)

    try:
        while True:
            s.update(wait=1.0/25)
            s.step += 1
            for c in chars: c.update()
    except KeyboardInterrupt:
        s.update(clear=True)
        s.putstr(prompt_text[-1] + "  ", typing=True)

try:
    curses.wrapper(main)
except curses.error as e:
    from sys import stderr
    print("Error: %s" % e, file=stderr)
except KeyboardInterrupt:
    pass
