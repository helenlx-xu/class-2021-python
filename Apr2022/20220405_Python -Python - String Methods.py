print("---------------------------1---------------------------")
#Python String find() Method：
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
print("---------------------------2---------------------------")
#Python String index() Method
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Hello, welcome to my world." 
x = txt.index("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)
print("---------------------------3---------------------------")
#Python String join() Method
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
print("---------------------------4---------------------------")
#Python String rsplit() Method
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)