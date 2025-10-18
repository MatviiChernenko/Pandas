# напиши тут код створення та управління карткою
class Mapmaneger():
    def __init__(self):
        self.model = "block.egg"
        self.texture = "block.png"

def addBlock(self,position):
    self.block = loader.loadModel(self.model)
    self.block.setTexture(loader.loadTexture(self.texture))
    self.block.setPos(position)
    self.block.reparentTo(render)