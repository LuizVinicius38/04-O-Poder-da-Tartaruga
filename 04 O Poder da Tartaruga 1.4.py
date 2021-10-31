from turtle import *

speed(11)
shape("turtle")
lados = 9
angulo = 360 / lados
for count in range(30):
    forward(50)
    left(angulo)

done()
