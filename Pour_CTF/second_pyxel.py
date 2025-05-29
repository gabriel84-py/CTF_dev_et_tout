import pyxel
from pyxel.pyxel_wrapper import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_SPACE, Tilemap


class Game:


    def __init__(self):

        pyxel.init(128, 128)
        pyxel.load("2.pyxres")
        self.sortie_1 = [110, 110]
        self.boss1_pts_vie = 100
        self.boss2_pts_vie = 100
        self.boss3_pts_vie = 100
        self.sortie_2 = [110, 50]
        self.sortie_3 = [110, 15]
        self.position_boss_1 = [90, 105]
        self.position_boss_2 = [90, 45]
        self.position_boss_3 = [90, 10]
        self.boss_atteindre = self.position_boss_1
        self.x = 1
        self.y = 110
        self.position = [self.x, self.y]
        self.col = 0
        self.fond = 1
        self.proche_boss_1 = 1
        self.proche_boss_2 = 1
        self.proche_boss_3 = 1
        self.présence_épée = 1
        self.position_épée = 1
        pyxel.run(self.update, self.draw)

    def distance_boss(self):

        if (self.position_boss_1[0] - self.x) <= 15 and self.position_boss_1[1] == 105 and self.boss1_pts_vie != 0:
            self.proche_boss_1 = 2
        elif (self.position_boss_2[0] - self.x) <= 15 and self.y == 50 and self.boss2_pts_vie != 0:
            self.proche_boss_2 = 2
        elif (self.position_boss_3[0] - self.x) <= 15 and self.y == 15 and self.boss3_pts_vie != 0:
            self.proche_boss_3 = 2

    def attaque_boss(self):
        self.présence_épée = 2
        if pyxel.btn(pyxel.KEY_SPACE):
            self.position_épée = 2
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.position_épée = 1
            if self.y == 110:
                self.boss1_pts_vie -= 10
            if self.y == 50:
                self.boss2_pts_vie -= 10
            if self.y == 15:
                self.boss3_pts_vie -= 10

            print(self.boss1_pts_vie)
        if self.boss1_pts_vie <= 0:
            print(self.boss1_pts_vie)
            self.proche_boss_1 = 1
        if self.boss2_pts_vie <= 0:
            self.proche_boss_2 = 1
        if self.boss3_pts_vie <= 0:
            self.proche_boss_3 = 1


    def sortie_atteinte(self):

        if self.position == self.sortie_1:
            self.x = 5
            self.y = 50

        elif self.position == self.sortie_2:
            self.x = 5
            self.y = 15

        elif self.position == self.sortie_3:
            self.fond = 2

    def draw(self):

        pyxel.cls(0)

        if self.fond == 1:
            pyxel.bltm(0, 0, 1, 0, 0, 248, 248 )
            pyxel.rectb(110, 110, 10, 10, 11)
            pyxel.rectb(110, 50, 10, 10, 11)
            pyxel.rectb(110, 15, 10, 10, 11)
            pyxel.rectb(5, 50, 10, 10, 8)
            pyxel.rectb(5, 15, 10, 10, 8)

            if self.boss1_pts_vie > 0:
                pyxel.blt(90, 105, 0, 128, 16, 16, 16, 2)


            if self.boss2_pts_vie > 0:
                pyxel.blt(90, 45, 0, 128, 16, 16, 16, 2)


            if self.boss3_pts_vie > 0:
                pyxel.blt(90, 10, 0, 128, 16, 16, 16, 2)


            pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16, 2)


        elif self.fond == 2:
            pyxel.bltm(0, 0, 2, 0, 0, 248, 248)
            pyxel.blt(60, 60, 0, 0, 16, 16, 16, 2)
            pyxel.text(5, 20, "Bravo tu as sauve", 0)
            pyxel.text(5, 45, "Bob le scaphandrier", 0)

        if self.présence_épée == 2:
            if self.position_épée == 1:
                pyxel.blt((self.x - 5), self.y, 0, 0, 64, -16,12, 2)
            elif self.position_épée == 2:
                pyxel.blt((self.x + 5), self.y, 0, 0, 64, 12, 12, 2)

    def update(self):

        if self.proche_boss_1 == 1 and self.proche_boss_2 == 1 and self.proche_boss_3 == 1:
            self.présence_épée = 1
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 1
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 1
            if self.fond == 1:
                self.sortie_atteinte()
                self.distance_boss()


        if self.proche_boss_1 == 2:
            self.attaque_boss()
        if self.proche_boss_2 == 2:
            self.attaque_boss()
        if self.proche_boss_3 == 2:
            self.attaque_boss()
        print(self.proche_boss_1, self.proche_boss_2, self.proche_boss_3)
        self.position = [self.x, self.y]

Game()
