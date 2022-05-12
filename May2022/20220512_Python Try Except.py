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


# 下面是自己写的代码
try:
  print(a)
except:
  print("b")


try:
  print(x)
except NameError:
  print("x没有被赋值")
except:
  print("123")


try:
  print("ABC")
except:
  print("Something went wrong")
else:
  print("nothing went wrong")



try:
  print(x)
except:
  print("there's something wrong")
finally:
  print("finished")