print(234//10)
print(234%10)

a = int(input())
b = int(input())
print(a,"+",b,"的结果为",a+b)

year = int(input("请输入一个年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("闰年")
else:
    print("平年")

a = int(input("请输入第一个数:"))
b = int(input("请输入第二个数:"))
if a > b:
    print("较大的数是",a)
else:
    print(b)