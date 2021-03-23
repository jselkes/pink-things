#study dice click

import random
from graphics import *

win = GraphWin('study dice click',500,300)
win.setCoords(0,0,10,6)
win.setBackground('white')

message = Text(Point(5,5),"click these cute dice to roll them")
message.setTextColor('IndianRed')
message.setFace('helvetica')
message.setSize(14)
message.draw(win)

dicefive = Rectangle(Point(1,1),Point(4,4))
dicefive.setFill('IndianRed')
dicefive.draw(win)

dicethree = Rectangle(Point(5,1),Point(8,4))
dicethree.setFill('IndianRed')
dicethree.draw(win)

#exit button and text
leave = Rectangle(Point(8.5,5),Point(10,6))
leave.setFill('light pink')
leave.setOutline('light pink')
leave.draw(win)

bye = Text(Point(9.25,5.5),"exit")
bye.setSize(14)
bye.setTextColor('IndianRed')
bye.draw(win)


def circ(x,y):
    center = Point(x,y)
    circ = Circle(center,.3)
    circ.setFill('light pink')
    return circ

#die one

#bottom right
t = circ(3.5,1.5)

#bottom left
u = circ(1.5,1.5)

#middle left
v = circ(1.5,2.5)

#middle right
w = circ(3.5, 2.5)
    
#middle
x = circ(2.5,2.5)

#top left
y = circ(1.5,3.5)

#top right
z = circ(3.5,3.5)



#die two

#bottom left
a = circ(5.5,1.5)

#top left
b = circ(5.5,3.5)

#top right
c = circ(7.5,3.5)

#bottom right
d = circ(7.5,1.5)

#middle
e = circ(6.5,2.5)

#middle left
f = circ(5.5, 2.5)

#middle right
g = circ(7.5,2.5)


    
X1=[x]
X2=[u,z]
X3=[u,x,z]
X4=[t,u,y,z]
X5=[t,u,x,y,z]
X6=[t,u,v,w,y,z]

def rollX(X):
    global J
    if X == 1:
        J = X1
        for i in X1:
            i.draw(win)
    elif X == 2:
        J = X2
        for i in X2:
            i.draw(win)
    elif X == 3:
        J = X3
        for i in X3:
            i.draw(win)
    elif X == 4:
        J = X4
        for i in X4:
            i.draw(win)
    elif X == 5:
        J = X5
        for i in X5:
            i.draw(win)
    elif X == 6:
        J = X6
        for i in X6:
            i.draw(win)

    return rollX

Y1=[e]
Y2=[a,c]
Y3=[a,e,c]
Y4=[a,b,c,d]
Y5=[a,b,c,d,e]
Y6=[a,b,c,d,f,g]

def rollY(Y):
    global L
    if Y == 1:
        L = Y1
        for i in Y1:
            i.draw(win)
    elif Y == 2:
        L = Y2
        for i in Y2:
            i.draw(win)
    elif Y == 3:
        L = Y3
        for i in Y3:
            i.draw(win)
    elif Y == 4:
        L = Y4
        for i in Y4:
            i.draw(win)
    elif Y == 5:
        L = Y5
        for i in Y5:
            i.draw(win)
    else:
        L = Y6
        for i in Y6:
            i.draw(win)

    return rollY

def undrawdice(J,L):
    for i in J:
        i.undraw()
    for i in L:
        i.undraw()

G = win.getMouse()

while G.getX() < 8.5 and G.getY() < 5:
    X = random.randint(1,6)
    Y = random.randint(1,6)
    rollX(X)
    rollY(Y)
    G = win.getMouse()
    undrawdice(J,L)


win.close()
