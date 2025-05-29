import pyxel
from pyxel.pyxel_wrapper import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_SPACE

class Game:

    def __init__(self):
        pyxel.init(160, 120)
        self.x = 60
        self.y = 60
        self.col = 0
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 16, 16, self.col)

    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.col += 1
            if self.col > 15:
                self.col = 0

    def sauter(self):


Game()
