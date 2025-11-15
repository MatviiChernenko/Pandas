# напиши тут код основного вікна гри
from mapmanager import Mapmaneger
from hero import Hero
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.maps = Mapmaneger()
        self.maps.load_land()
        self.hero = Hero(self.maps)
        self.task_mgr.add(self.update,"update")
        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)

    def update(self,task):
        self.hero.update()
        return task.cont

game = Game()
game.run()