from turtle import *

def flower():
    for i in range(200):
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)

flower()
mainloop()