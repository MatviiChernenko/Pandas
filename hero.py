# напиши свій код тут
class Hero():
    def __init__(self):
        self.hero = loader.loadModel("block.egg")
        self.hero.setTexture(loader.loadTexture("block.png"))
        self.hero.setColor((0.8, 0.9, 0 , 1))
        self.hero.setPos(10,20,3)
        self.hero.reparentTo(render)