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
        self.fond = 4
        self.proche_boss_1 = 1
        self.proche_boss_2 = 1
        self.proche_boss_3 = 1
        self.presence_epee = 1
        self.position_epee = 1
        self.costume = 0
        self.timer = 0
        self.explosion_liste = []
        self.y_depart = 0
        pyxel.play(0, 0, loop=True)
        pyxel.run(self.update, self.draw)


    def distance_boss(self):

        if (self.position_boss_1[0] - self.x) <= 15 and self.position_boss_1[1] == 105 and self.boss1_pts_vie != 0:
            self.proche_boss_1 = 2

        elif (self.position_boss_2[0] - self.x) <= 15 and self.y == 50 and self.boss2_pts_vie != 0:
            self.proche_boss_2 = 2

        elif (self.position_boss_3[0] - self.x) <= 15 and self.y == 15 and self.boss3_pts_vie != 0:
            self.proche_boss_3 = 2

    def attaque_boss(self):
        self.presence_epee = 2
        if pyxel.btn(pyxel.KEY_SPACE):
            self.position_epee = 2
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.position_epee = 1
            if self.y == 110:
                self.boss1_pts_vie -= 10
            if self.y == 50:
                self.boss2_pts_vie -= 10
            if self.y == 15:
                self.boss3_pts_vie -= 10


        if self.boss1_pts_vie <= 0:

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

        pyxel.cls(7)

        if self.fond == 4:
            pyxel.bltm(0,0,4,0,0,248,248, 2)
            pyxel.text(1, 57, "Bob va plonger,", 0)
            pyxel.text(1, 65, " mais il n'a que 22 sec d'air,", 0)
            pyxel.text(1, 73, "aide le a rejoindre la surface", 0)
            pyxel.text(1, 81, "avant qu'il ne manque d'oxygene!", 0)     
            pyxel.text(15, 113, "Appuyez sur espace", 0)
            pyxel.text(1, 97, "Avancer/reculer: utiliser les flèches", 0)
            pyxel.text(1, 105, "Attaque : appuyer sur espace", 0)

        elif self.fond == 5:
            pyxel.bltm(0,0, 1, 0, 0, 248, 248)
            pyxel.blt(self.x, self.y_depart, 0, 0, 16, 16, 16, 2)

        elif self.fond == 1:
            pyxel.bltm(0, 0, 1, 0, 0, 248, 248 )
            pyxel.rectb(110, 110, 10, 10, 11)
            pyxel.rectb(110, 50, 10, 10, 11)
            pyxel.rectb(110, 15, 10, 10, 11)
            pyxel.rectb(5, 50, 10, 10, 8)
            pyxel.rectb(5, 15, 10, 10, 8)
            pyxel.text(1, 1, f'Timer : {str(self.timer)}', 0)


            if self.boss1_pts_vie > 0:
                pyxel.blt(90, 105, 0, 128, 16, 16, 16, 2)


            if self.boss2_pts_vie > 0:
                pyxel.blt(90, 45, 0, 128, 16, 16, 16, 2)


            if self.boss3_pts_vie > 0:
                pyxel.blt(90, 10, 0, 128, 16, 16, 16, 2)


            if self.costume == 0:
                pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16, 2)
            elif self.costume == 1:
                pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16, 2)
            elif self.costume == 2:
                pyxel.blt(self.x, self.y, 0, 16, 48, 16, 16, 2)


        elif self.fond == 2:
            pyxel.bltm(0, 0, 2, 0, 0, 248, 248, 2 )
            pyxel.blt(58, 58, 0, 0, 16, 16, 16, 2)
            pyxel.text(25, 20, "Bravo tu as sauve", 0)
            pyxel.text(21, 30, "Bob le scaphandrier !", 0)

        elif self.fond == 3:
            pyxel.bltm(0, 0, 3, 0, 0, 248, 248)
            pyxel.text(13, 35, "Baaaaaaaaaah t'es nuuul !!!", 0)
            pyxel.blt(58, 58, 0, 80, 32, 16, 16, 2)


        if self.presence_epee == 2:
            if self.position_epee == 1:
                pyxel.blt((self.x - 5), self.y, 0, 0, 64, -16,12, 2)
            elif self.position_epee == 2:
                pyxel.blt((self.x + 5), self.y, 0, 0, 64, 12, 12, 2)





    def update(self):

        if self.fond == 4 and pyxel.btn(KEY_SPACE):
            self.fond = 5

        elif self.fond == 5:
            if int(pyxel.frame_count / 1) == (pyxel.frame_count / 1) and self.y_depart != self.y:
                self.y_depart += 1
            elif self.y == self.y_depart:
                self.fond = 1

        if self.proche_boss_1 == 1 and self.proche_boss_2 == 1 and self.proche_boss_3 == 1:
            self.presence_epee = 1
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 1
                self.costume = (self.costume + 1) % 2
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 1
                self.costume = (self.costume + 1) % 2
            if self.fond == 1:
                self.sortie_atteinte()
                self.distance_boss()

        if int(pyxel.frame_count / 30) == (pyxel.frame_count / 30) and self.fond == 1:
            self.timer += 1
        if self.fond == 1:
            if self.timer == 22:
                self.fond = 3

        if self.proche_boss_1 == 2:
            self.attaque_boss()
        if self.proche_boss_2 == 2:
            self.attaque_boss()
        if self.proche_boss_3 == 2:
            self.attaque_boss()

        self.position = [self.x, self.y]

Game()