from turtle import Turtle
from types import LambdaType


class table:
  def __init__(self, color, width, length, age, height, brand,lamp,study):
    self.color = color
    self. width = width
    self. length = length
    self. height = height
    self. age = age
    self. brand = brand
    self. lamp = lamp
    self. study = study

p1 = table("while",60,140,100,6,"mini",'Ture','Ture')

print(p1.color)
print(p1.width)
print(p1.length)
print(p1.height)
print(p1.age)
print(p1.brand)
print(p1.lamp)
print(p1.study)
