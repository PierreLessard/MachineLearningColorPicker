from turtle import *
import random
import pickle
from time import sleep

def reset_batch_data():
    batch_data_x = []
    batch_data_y = []

    with open('batch_data_rgb.txt', 'wb') as fp:
        pickle.dump(batch_data_x, fp)
    
    with open('batch_data_color.txt', 'wb') as fp:
        pickle.dump(batch_data_y, fp)

def open_batch_data(filename):
    with open (filename, 'rb') as fp:
        batch_data = pickle.load(fp)
        return(batch_data)

def append_batch_data(rgb,color):
    with open ('batch_data_rgb.txt', 'rb') as fp:
        batch_data_rgb = pickle.load(fp)

    batch_data_rgb.append(rgb)

    with open ('batch_data_color.txt', 'rb') as fp:
        batch_data_color = pickle.load(fp)

    batch_data_color.append(color)

    with open('batch_data_rgb.txt', 'wb') as fp:
        pickle.dump(batch_data_rgb, fp)
    
    with open('batch_data_color.txt', 'wb') as fp:
        pickle.dump(batch_data_color, fp)


window = Screen()

window.tracer(0)
t = Turtle()
t.hideturtle()

t.goto(-750,-750)
window.colormode(255)

t.fillcolor(100,100,100)
t.begin_fill()
for r in range(4):
    t.forward(1500)
    t.left(90)
t.end_fill()

t.color('white')

window.colormode(255)

class Square:

    def __init__(self):
        self.rgb = [0,0,0]
    
    def randomize(self):
        r,g,b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
        self.rgb = [r,g,b]
    
    def draw(self):
        t.up()
        t.goto(-200,-100)
        t.down()
        window.colormode(255)
        t.fillcolor(self.rgb[0],self.rgb[1],self.rgb[2])
        
        t.begin_fill()
        for i in range(4):
            t.forward(400)
            t.left(90)
        t.end_fill()
        t.forward(10)

square = Square()
square.randomize()
square.draw()

class Button:
    
    def __init__(self,color,x,y):
        self.color = color
        self.x = x
        self.y = y
        self.l = 75
    
    def check(self,x,y):
        check = 0
        if x > self.x:
            if y > self.y:
                if y < self.y + self.l:
                    if x < self.x + self.l:
                        check = 1
        return(check)

    def draw(self):
        t.up()
        t.goto(self.x,self.y)
        t.down()
        window.colormode(0)
        #t.fillcolor(self.color)
        t.fillcolor('darkgrey')

        t.begin_fill()
        for i in range(4):
            t.forward(self.l)
            t.left(90)
        t.end_fill()
        t.forward(10)

        t.write(self.color)


black = Button('black',-250,-250)
blue = Button('blue',-175,-250)
brown = Button('brown',-100,-250)
cyan = Button('cyan',-25,-250)
green = Button('green',50,-250)
gray = Button('gray',125,-250)
magenta = Button('magenta',200,-250)
orange = Button('orange',-250,-175)
pink = Button('pink',-175,-175)
purple = Button('purple',-100,-175)
red = Button('red',-25,-175)
white = Button('white',50,-175)
yellow = Button('yellow',125,-175)

color_buttons = [black,blue,brown,cyan,green,gray,magenta,orange,pink,purple,red,white,yellow]


for button in color_buttons:
    button.draw()

def main(x,y):
    for button in color_buttons:
        check  = button.check(x,y)

        if check == 1:
            print(button.color)
            print(square.rgb)

            append_batch_data(square.rgb,[button.color])

            square.randomize()
            square.draw()
        if check == 2:
            square.randomize()
            square.draw()


y=open_batch_data('batch_data_color.txt')
x=open_batch_data('batch_data_rgb.txt')
print(len(x))

window.onclick(main)
mainloop()