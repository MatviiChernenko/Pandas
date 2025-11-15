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
        self.block.setTag("at", str(position))
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

    def find_block(self,pos):
        return render.findAllMatches("=at=" + str(pos))
    
    def isEmpty(self,pos):
        block = self.find_block(pos)
        if block:
            return False
        else:
            return True
        
    def findLand(self,pos):
        x,y,z = pos
        z = 1
        while not self.isEmpty((x,y,z)):
            z += 1
        return (x,y,z)
    
    def place_block(self,pos):
        if self.isEmpty(pos):
            self.addBlock(self.findLand(pos))

    def remove_block(self,pos):
        blocks = self.find_block(pos)
        for block in blocks:
            block.removeNode()
    
    def remove_blocks(self,pos):
        x,y,z = self.findLand(pos)
        pos = x,y, z - 1
        for block in self.find_block(pos):
            block.removeNode()
