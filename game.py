# напиши тут код основного вікна гри
from mapmanager import Mapmaneger
from hero import Hero
from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.maps = Mapmaneger()
        self.maps.load_land()
        self.hero = Hero()

game = Game()
game.run()