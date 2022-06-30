try:
  print(x)
except:
  print("An exception occurred")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#自己写的
try:
  print(x)
except:
  print("haha")

try:
  print(x)
except NameError:
  print("1")
except:
  print("2")


try:
  print("Hello")
except:
  print("hello")
else:
  print("h")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
