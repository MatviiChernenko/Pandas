# напиши тут код основного вікна гри
from mapmanager import Mapmaneger
from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.maps = Mapmaneger()

game = Game()
game.maps.addBlock((0,0,0))
game.maps.addBlock((0,0,1))
game.maps.addBlock((0,1,0))
game.maps.addBlock((1,1,0))
game.run()