#!/usr/bin/python

from curses import color_pair, error
from random import randrange as rr

class MatrixChar(object):

    def __init__(self, char=' ', *args, **kwargs):
        self.char = char

    @classmethod
    def setscreen(cls, scr):
        cls.scr = scr

    @classmethod
    def get(cls, num):
        return tuple(cls() for i in range(num))

    @property
    def c(self):
        return self.y, self.x, self.char, self.attr

    def newpos(self, top=False):
        self.y, self.x = self.scr.randpos
        if top: self.y = 0

    def put(self, hlight=False):
        self.attr = color_pair(2 if hlight else 1)
        try:
            self.__class__.scr.put(self)
        except error:
            self.update(reset=True)


class BlankChar(MatrixChar):

    def update(self, reset=False):
        self.newpos()
        if not reset: self.put()


class RainChar(MatrixChar):

    HW_KANA = 'ｦｧｨｩｪｫｬｭｮｯｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ'

    def __init__(self, speedlimit=(1, 8)):
        super().__init__()
        self.speedlimit = speedlimit
        if self.char is ' ':
            self.chars = self.HW_KANA
        else:
            self.chars = self.char
        self.num_c = len(self.chars)
        self.top = False

    def newchar(self):
        self.char = self.chars[rr(self.num_c)]

    def update(self, reset=False):
        if reset or not self.top:
            self.newpos(top=self.top)
            if not self.top: self.top = True
            self.newchar()
            self.speed = rr(*self.speedlimit)
            self.speed += rr(self.speed)
        elif self.scr.step % self.speed:
            return
        self.put()
        self.y += 1
        self.newchar()
        self.put(True)