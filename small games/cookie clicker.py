import os
import turtle

window = turtle.Screen()
window.setup(800,800)
window.title("cookie Clicker")
window.bgcolor("black")
window.register_shape(r'C:\Users\HP\Downloads\cookie.gif')


cookie = turtle.Turtle()
cookie.shape(r'C:\Users\HP\Downloads\cookie.gif')
cookie.speed(0)
clicks= 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,300)
pen.write(f"Clicks:{clicks}", align="center", font=("Courier New", 32 ,"normal"))

def clicked(x,y):
    global clicks
    clicks +=1
    pen.clear()
    pen.write(f"Clicks:{clicks}", align="center", font=("Courier New", 32, "normal"))

cookie.onclick(clicked)

window.mainloop()
