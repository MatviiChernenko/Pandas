# напиши тут код створення та управління карткою
class Mapmaneger():
    def __init__(self):
        self.model = "block.egg"
        self.texture = "block.png"
        self.file = "land2.txt"

    def addBlock(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.reparentTo(render)

    def load_land(self):
        x,y = 0,0
        with open(self.file) as file:
            string_list = file.readlines()
            for string in string_list:
                x = 0
                int_list = list(map(int, string.split(" ")))
                for element in int_list:
                    for z in range(element + 1):
                        self.addBlock((x,y,z))
                    x += 1
                y += 1
