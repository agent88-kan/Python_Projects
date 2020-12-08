from turtle import *
def turtlecontrol(where, howmuch):
    where = where.upper()
    if where == "F":
        forward(howmuch)
    elif where == "B":
        backward(howmuch)
    elif where == "R":
        right(howmuch)
    elif where == "L":
        left(howmuch)
    elif where == "N":
        reset()
    elif where == "PD":
        pendown()
    elif where == "PU":
        penup()
    else:
        print("Error 404 ; Command not found")
def stringcontrol(commands):
    commandlist = commands.split("-")
    for commands in commandlist:
        listlength = len(commands)
        if listlength == 0:
            continue
        commandtype = commands[0]
        number = 0
        if listlength > 1:
            numbertext = commands[1:]
            number = int(numbertext)
        print(commands, ":", commandtype, number)
        turtlecontrol(commandtype, number)
revealer = '''Write the commands for the turtle:
example: F100-R45-PU-F100-L45-PD-F100-R90-B50
N = new paper 
PU = penup
PD = pendown
F100 = forward 100
B50 = backward 50
R90 = right 90 degree
L45 = left 45 degree'''
screen = getscreen()
screen.title("drawingMachine by agent88-kan")
while True:
    turtletask = screen.textinput("drawingMachine by agent88-kan", revealer)
    print(turtletask)
    if turtletask == None or turtletask.upper() == "CANCEL":
        break
    stringcontrol(turtletask)