#what time will the alarm go off?


from graphics import *

win = GraphWin('nap clock',500,500)
win.setCoords(0,0,20,20)
win.setBackground('pink')

#entry boxes
entry1 = Entry(Point(10,15),10)
entry1.setSize(18)
entry1.setTextColor('black')
entry1.draw(win)

entry2 = Entry(Point(10,11),10)
entry2.setSize(18)
entry2.setTextColor('black')
entry2.draw(win)


#button and button text
button = Rectangle(Point(9,7),Point(11,9))
button.setFill('IndianRed')
button.draw(win)

click = Text(Point(10,8),"Start")
click.setSize(14)
click.setTextColor('white')
click.draw(win)


#exit button and text
exb = Rectangle(Point(18,0),Point(20,2))
exb.setFill('IndianRed')
exb.draw(win)

leave = Text(Point(19,1),"Exit")
leave.setSize(14)
leave.setTextColor('white')
leave.draw(win)


#prompt
prompt1 = Text(Point(10,17),"What time is it?")
prompt1.setSize(20)
prompt1.setTextColor('black')
prompt1.draw(win)

prompt2 = Text(Point(10,13),"How long will you nap?")
prompt2.setSize(20)
prompt2.setTextColor('black')
prompt2.draw(win)


G = win.getMouse()

while G.getX() < 18 and G.getY() > 2:
    result = 0
    if 9 <= G.getX() <= 11 and 7 <= G.getY() <= 9:
        x = int(entry1.getText())
        y = int(entry2.getText())
        wakeup = x+y
        if wakeup != 12:
            wakeup = wakeup % 12    
        result = Text(Point(10,5),"Alarm will go off at "+ str(wakeup))
        result.setSize(25)
        result.setTextColor('IndianRed')
        result.draw(win)

    G = win.getMouse()
    if result != 0:
        result.undraw()

    

if 18 <= G.getX() <= 20 and 0 <= G.getY() <= 2:
        win.close()
    
