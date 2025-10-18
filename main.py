from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel("block.egg")
        self.model.setTexture(loader.loadTexture("block.png"))
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(0,100,-10)

geme = Game()
geme.run()