print("---------------------------1---------------------------")
print("Hello")
print('Hello')
print("---------------------------2---------------------------")
a = "Hello"
print(a)
print("---------------------------3---------------------------")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("---------------------------4---------------------------")
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print("---------------------------5---------------------------")
a = "Hello, World!"
print(a[1])
print("---------------------------6---------------------------")
for x in "banana":
  print(x)
print("---------------------------7---------------------------")
a = "Hello, World!"
print(len(a))
print("---------------------------8---------------------------")
txt = "The best things in life are free!"
print("free" in txt)
print("---------------------------9---------------------------")
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
print("---------------------------10---------------------------")
txt = "The best things in life are free!"
print("expensive" not in txt)
print("---------------------------11---------------------------")
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")