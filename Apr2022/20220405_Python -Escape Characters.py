print("---------------------------1---------------------------")
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
print("---------------------------2---------------------------")
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
print("---------------------------3---------------------------")
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)
print("---------------------------4---------------------------")
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
print("---------------------------5---------------------------")
txt = "Hello\tWorld!"
print(txt) 
print("---------------------------6---------------------------")
txt = "Hello\rWorld!"
print(txt) 
print("---------------------------7---------------------------")
txt = "Hello\nWorld!"
print(txt) 
print("---------------------------8---------------------------")
txt = 'It\'s alright.'
print(txt) 
print("---------------------------9---------------------------")
txt = "This will insert one \\ (backslash)."
print(txt) 