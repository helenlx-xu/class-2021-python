# class MyClass:
#   x = 5

# print(MyClass)


# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)



# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)

# p1.age = 40

# print(p1.age)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()



#下面是自己写的代码

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

#_init_(self)初始化函数
#_init_()方法是所谓的对象的“构造函数”
#_init_()