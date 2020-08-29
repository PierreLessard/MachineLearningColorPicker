import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import pickle
from turtle import *
import random

def open_batch_data(filename):
    with open (filename, 'rb') as fp:
        batch_data = pickle.load(fp)
        return(batch_data)

colors = open_batch_data('batch_data_color.txt')
rgb = open_batch_data('batch_data_rgb.txt')

model = open_batch_data('color_model.pkl')

rgb_pred = model.predict(rgb)
accuracy=accuracy_score(y_true=colors, y_pred=rgb_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

window = Screen()
window.tracer(0)
t = Turtle()
t.hideturtle()
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

def main(x,y):
    t.goto(-750,-750)
    t.fillcolor(100,100,100)
    t.begin_fill()
    for r in range(4):
        t.forward(1500)
        t.left(90)
    t.end_fill()

    square.randomize()
    square.draw()

    t.goto(-200,-200)
    t.write(model.predict([square.rgb]))

square = Square()
main(0,0)

window.onclick(main)
mainloop()