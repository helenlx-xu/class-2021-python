def get_sum(*args):
    total = 0
    for i in args:
        total += i

    print('内部:',total)
    return total


t = get_sum(1, 2, 3)
print('外侧:',t)

x = 100
x = x + t
print(x)