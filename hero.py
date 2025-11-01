# напиши свій код тут

camera = "c"
mode = "m"
forward = 'w'
backward = "s"
left = "a"
right = "d"

rotate_left = "arrow_left"
rotate_right = "arrow_right"
up = "q"
down = "e"

class Hero():
    def __init__(self):
        self.cameraOn = True
        self.mode = True
        self.hero = loader.loadModel("block.egg")
        self.hero.setTexture(loader.loadTexture("skeleton_130x130.png"))
        self.hero.setPos(10,20,3)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0],-pos[1],-pos[2] - 2)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def camera_change(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def lokAt(self,angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())

        dx, dy = self.checkDir(angle)

        return(x + dx,y + dy,z)

    def checkDir(self,angle):
        if angle <= 20:
            return (0,-1)
        elif angle <= 65:
            return(1,-1)
        elif angle <= 110:
            return(1,0)
        elif angle <= 155:
            return(1,1)
        elif angle <= 200:
            return(0,1)
        elif angle <= 245:
            return(-1,1)
        elif angle <= 290:
            return(-1,0)
        elif angle <= 335:
            return(-1,-1)
        else:
            return(0,-1)

    def tryMove(self,angle):
        pass

    def justMove(self,angle):
        pos = self.lokAt(angle)
        self.hero.setPos(pos)

    def moveTo(self,angle):
        if self.mode:
            self.tryMove(angle)
        else:
            self.justMove(angle)

    def chageMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def forward(self):
        angle = self.hero.getH() % 360
        self.moveTo(angle)

    def backward(self):
        angle = (self.hero.getH()+180) % 360
        self.moveTo(angle)

    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.moveTo(angle)

    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.moveTo(angle)

    def rotateLeft(self):
        self.hero.setH(self.hero.getH()+5)

    def rotateRight(self):
        self.hero.setH(self.hero.getH()-5)


    def accept_events(self):
        base.accept(camera,self.camera_change)
        base.accept(mode,self.chageMode)

        base.accept(rotate_left,self.rotateLeft)
        base.accept(rotate_left + "-repeat",self.rotateLeft)
        base.accept(rotate_right,self.rotateRight)
        base.accept(rotate_right + "-repeat",self.rotateRight)
        base.accept(forward, self.forward)
        base.accept(forward + "-repeat",self.forward)
        base.accept(backward, self.backward)
        base.accept(backward + "-repeat",self.backward)
        base.accept(left, self.left)
        base.accept(left + "-repeat",self.left)
        base.accept(right, self.right)
        base.accept(right + "-repeat",self.right)
