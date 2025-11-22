# напиши свій код тут
from math import *

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

create_block = "mouse1"
remove_block = "mouse3"

save_map = "control-s"
load_map = "control-o"


def degreeToRadian(angle):
    return angle *(pi / 180)

class Hero():
    def __init__(self,land):
        self.land = land
        self.cameraOn = True
        self.mode = True
        self.pitch = 0
        self.roll = 0
        self.speed = 0.05
        self.move ={
            "forward": False,
            "backward": False,
            "left": False,
            "right": False
        }
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

    def lookAt(self,angle):
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

    def tryMove(self,x,y):
        pos = round(x), round(y), round(self.hero.getZ())

        if self.land.isEmpty(pos):
            pos = self.land.findLand(pos)
            return pos[2], True
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                return pos[2], True
            return self.hero.getZ(), False

    def justMove(self,angle):
        pos = self.lookAt(angle)
        self.hero.setPos(pos)

    #def moveTo(self,angle):
    #    if self.mode:
    #        self.tryMove(angle)
    #    else:
    #        self.justMove(angle)

    def chageMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    """    def forward(self):
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
"""


    def update_key(self,key,value):
        self.move[key] = value


    def update(self):
        speedX = 0
        speedY = 0
        speedZ = 0

        z = 0
        if self.cameraOn:
            if base.mouseWatcherNode.hasMouse():
                x = base.mouseWatcherNode.getMouseX()
                y = base.mouseWatcherNode.getMouseY()
                prop = base.win.getProperties()
                base.win.movePointer(0, prop.getXSize() // 2, prop.getYSize() // 2)
                self.pitch -= x*30
                self.hero.setH(self.pitch)
                self.roll -= y*30
                self.roll = max(min(self.roll,90), -90)
                self.hero.setP(self.roll)
            if self.move["forward"]:
                speedX += cos(degreeToRadian(self.hero.getH() - 90))
                speedY += cos(degreeToRadian(self.hero.getH() - 180))
            if self.move["backward"]:
                speedX += cos(degreeToRadian(self.hero.getH() - 270))
                speedY += cos(degreeToRadian(self.hero.getH() - 0))
            if self.move["left"]:
                speedX += cos(degreeToRadian(self.hero.getH() - 0))
                speedY += cos(degreeToRadian(self.hero.getH() - 90))
            if self.move["right"]:
                speedX += cos(degreeToRadian(self.hero.getH() - 180))
                speedY += cos(degreeToRadian(self.hero.getH() - 270))

            if self.mode and True in list(self.move.values()):
                posZ = self.tryMove(self.hero.getX() + (speedX * self.speed), self.hero.getY() + (speedY * self.speed))
                if posZ[1]:
                    self.hero.setZ(posZ[0])
                else:
                    speedX = 0
                    speedY = 0
            if not self.mode and True in list(self.move.values()):
                speedX *= abs(cos(degreeToRadian(self.hero.getP())))
                speedY *= abs(cos(degreeToRadian(self.hero.getP())))
                if self.move["forward"]:
                    speedZ = sin(degreeToRadian(self.hero.getP())) * -1
                else:
                    speedZ = sin(degreeToRadian(self.hero.getP()))
            modul = ((speedX ** 2) + (speedY ** 2) + (speedZ ** 2)) ** 0.5
            if modul == 0:
                k = 1
            else:
                k = self.speed/modul

            self.hero.setPos(self.hero.getPos() + (k * speedX, k * speedY, k * speedZ))

            
    def modeBuild(self):
        if self.mode:
            self.land.place_block(self.lookAt(self.hero.getH() % 360))
        else:
            self.land.addBlock(self.lookAt(self.hero.getH() % 360))

    def modeDestroy(self):
        if self.mode:
            self.land.remove_blocks(self.lookAt(self.hero.getH() % 360))
        else:
            self.land.remove_block(self.lookAt(self.hero.getH() % 360))




    def accept_events(self):
        base.accept(camera,self.camera_change)
        base.accept(mode,self.chageMode)
        base.accept(create_block,self.modeBuild)
        base.accept(remove_block,self.modeDestroy)
        base.accept(load_map,self.land.load_map)
        base.accept(save_map,self.land.save_map)




        base.accept(forward,self.update_key,["forward", True])
        base.accept(forward + "-up",self.update_key,["forward", False])
        base.accept(backward,self.update_key,["backward", True])
        base.accept(backward + "-up",self.update_key,["backward", False])
        base.accept(left,self.update_key,["left", True])
        base.accept(left + "-up",self.update_key,["left", False])
        base.accept(right,self.update_key,["right", True])
        base.accept(right + "-up",self.update_key,["right", False])

        #base.accept(rotate_left,self.rotateLeft)
        #base.accept(rotate_left + "-repeat",self.rotateLeft)
        #base.accept(rotate_right,self.rotateRight)
        #base.accept(rotate_right + "-repeat",self.rotateRight)
        #base.accept(forward, self.forward)
        #base.accept(forward + "-repeat",self.forward)
        #base.accept(backward, self.backward)
        #base.accept(backward + "-repeat",self.backward)
        #base.accept(left, self.left)
        #base.accept(left + "-repeat",self.left)
        #base.accept(right, self.right)
        #base.accept(right + "-repeat",self.right)
