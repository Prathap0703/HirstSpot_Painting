# import colorgram
# rgb_colors = []
# colors = colorgram.extract("img.jpeg",20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle

color_list = [(142, 77, 52), (188, 165, 118), (165, 152, 38), (16, 46, 83), (46, 110, 135), (144, 57, 83),
              (61, 120, 100), (143, 184, 174), (141, 170, 176), (86, 36, 30), (65, 152, 168), (219, 209, 96),
              (109, 38, 32), (102, 145, 110), (166, 98, 130), (95, 122, 169)]

from turtle import Turtle , Screen
import random

turtle.colormode(255)
prathu = Turtle()
prathu.speed("fastest")
prathu.penup()
prathu.hideturtle()
prathu.setheading(225)
prathu.forward(310)
prathu.setheading(0)

number_of_dots = 101
for dot in range(1, number_of_dots):
    prathu.dot(15,random.choice(color_list))
    prathu.forward(50)
    if dot % 10 == 0:
        prathu.setheading(90)
        prathu.forward(50)
        prathu.setheading(180)
        prathu.forward(500)
        prathu.setheading(0)




my_screen = Screen()
my_screen.exitonclick()