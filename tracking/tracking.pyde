"""
Circle Collision with Swapping Velocities.
by Ira Greenberg.
  
Based on Keith Peter's Solution in
"Foundation Actionscript Animation: Making Things Move!".
"""
from ball import Ball
import csv
add_library('video')

numBalls = 2
balls = []
tris = []
data = []

paused = True
curBall = -1
WIDTH = 2704
HEIGHT = 1520

MODE = 1

subID = ""

videoFilename = "test.mp4"
showingText = True

def setup():
    size(int(WIDTH*0.4), int(HEIGHT*0.4) + 100)
    background(0)
    frameRate(10)
    global movie
    movie = Movie(this, videoFilename)
    movie.pause()
    movie.loop()
    
    text("Click to add triangles, click on circle in triangle to toggle individual", 0, height - 80)
    text("While individual selected: Use left/right arrow keys to change angle of triangle, 't' to toggle talking status", 0, height - 60)
    text("Spacebar to pause video, 'h' to toggle show/hide video, as well as triangle IDs", 0, height - 40)
    text("Down arrow key to go back 10 seconds, 'q' to export data to csv", 0, height - 20)

def movieEvent(m):
    m.read()

def draw(): 
    global showingText
    if MODE == 1: 
        image(movie, 0,0,width,height - 100)
    if MODE == 0:
        background(0)
        if not showingText: 
            text("Click to add triangles, click on circle in triangle to toggle individual", 0, height - 80)
            text("While individual selected: Use left/right arrow keys to change angle of triangle, 't' to toggle talking status", 0, height - 60)
            text("Spacebar to pause video, 'h' to toggle show/hide video, as well as triangle IDs", 0, height - 40)
            text("Down arrow key to go back 10 seconds, 'q' to export data to csv", 0, height - 20)
            showingText = True
        for ball in balls:
            ball.displayID()
        
    if paused: 
        movie.pause()
    else: 
        movie.play()
        dataRow = [movie.time()]
        dataRow.append([[ball.ID, (ball.position.x ,ball.position.y), ball.angle, ball.talking] for ball in balls])
        data.append(dataRow)
    
    for ball in balls:
        ball.updateTri()
        ball.display()
        ball.checkBoundaryCollision()
    
    stroke(255)
    line(0, height-100, width, height-100)
    fill(255)
    
def keyPressed():
    global paused
    global movie
    global MODE
    global showingText
    global subID
    
    if isNum(key):
        subID += key
        
    if key == ENTER and curBall >= 0:
        balls[curBall].setID(int(subID))
        subID = ""
        
    if key == ' ':
        if not paused: 
            paused = True
        else: 
            paused = False
            
    if key == 'h':
        showingText = False
        MODE = abs(MODE-1)
        
    if key == 't':
        balls[curBall].talking = not balls[curBall].talking
        
    if key == 'q':
        with open('tracking_data_' + videoFilename.split(".")[0] + '.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for t in data: 
                writer.writerow(t)
    
    if key == BACKSPACE and curBall >=0: 
        del balls[curBall]
            
    if (key == CODED):
        if (keyCode == RIGHT) and curBall >= 0:
            balls[curBall].rotateRight()
            
        if (keyCode == LEFT) and curBall >= 0:
            balls[curBall].rotateLeft()
            
        if (keyCode == DOWN):
            movie.jump(movie.time()-10)
            del data[-100:]

def isNum(button):
    nums = [str(x) for x in range(10)]
    if button in nums: return True
    else: return False
    
def mouseClicked():
    global curBall
    for i in range(len(balls)): 
        if mouseInShape(mouseX, mouseY, balls[i].position.x, balls[i].position.y, balls[i].radius):
            if i == curBall: 
                balls[curBall].fillcol = 255
                balls[curBall].triColor = 255
                curBall = -1
            else:
                balls[curBall].fillcol = 255
                balls[curBall].triColor = 255
                curBall = i
                balls[curBall].fillcol = color(255,0,0)
                balls[curBall].triColor = color(255,0,0)
            return
    
    balls.append(Ball(len(balls) + 1, 5, mouseX, mouseY))

def mouseDragged():
    if curBall >= 0:
        balls[curBall].updatePos(mouseX, mouseY)
        
def mouseInShape(mX, mY, shapeX, shapeY, shapeR):
    if mX < (shapeX + shapeR) and mX > (shapeX - shapeR) and mY < (shapeY + shapeR) and mY > (shapeY - shapeR):
        return True
    return False
