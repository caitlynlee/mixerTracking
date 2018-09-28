from random import randint, random

r1=25
r2=10

class Ball(object):

    def __init__(self, ID, radius, x, y):
        self.ID = ID
        self.position = PVector(x, y)
        self.velocity = PVector(0,0)
        self.radius = radius
        self.m = self.radius * 0.1
        self.fillcol = 255
        self.triColor = 255
        self.talking = False
        self.angle = 0
        self.tri = (self.position.x - r1 * cos(self.angle), self.position.y - r1 * sin(self.angle),
                 self.position.x + r1 * cos(self.angle), self.position.y + r1 * sin(self.angle),
                 self.position.x + r2 * cos(self.angle + PI/2), self.position.y + r2 * sin(self.angle + PI/2))

    def updateTri(self):
        self.tri = (self.position.x - r1 * cos(self.angle), self.position.y - r1 * sin(self.angle),
                 self.position.x + r1 * cos(self.angle), self.position.y + r1 * sin(self.angle),
                 self.position.x + r2 * cos(self.angle + PI/2), self.position.y + r2 * sin(self.angle + PI/2))
    
    def setID(self, newID):
        self.ID = newID
    
    def rotateRight(self):
        self.angle -= PI/20
        self.updateTri()
        
    def rotateLeft(self):
        self.angle += PI/20
        self.updateTri()
        
    def updatePos(self, newX, newY):
        self.position = PVector(newX, newY)
        
    def checkBoundaryCollision(self):
        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -1
        elif self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= -1
        elif self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= -1
        elif self.position.y < self.radius:
            self.position.y = self.radius
            self.velocity.y *= -1

    def display(self):
        noStroke()
        fill(self.fillcol)
        ellipse(self.position.x, self.position.y, self.radius * 2, self.radius * 2)
        stroke(self.triColor)
        if not self.talking:
            noFill()
        triangle(*self.tri)
        
    def displayID(self):
        fill(255)
        text(self.ID, self.position.x - 10, self.position.y - 10)
