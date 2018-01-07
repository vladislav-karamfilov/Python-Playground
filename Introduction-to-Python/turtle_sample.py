import turtle
import math

turtle.speed('fastest')

colors = ['red', 'green', 'blue', 'purple']

for a in range(4):
    turtle.color(colors[a])
    x = 1
    for _ in range(1, 100):
        turtle.forward(10)
        turtle.right(100 - x)
        x += 1

g = 134
l = 120

i = 0
iterations_count = int(input('Enter iterations count: '))

while i < iterations_count:
    turtle.left(g)
    turtle.forward(l)
    i += 1

turtle.speed('fastest')

i = 10
while i < 1400 * math.pi:
    turtle.left(i % (math.pi * 100))
    turtle.forward(10)
    i += math.pi
