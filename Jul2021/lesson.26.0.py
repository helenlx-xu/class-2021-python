n = 1
while n <= 10:
    print('n')
    n += 1
else:            #else的特点：不中断则执行，若中断不执行
    print('over')

    n = 1
while n <= 10:
    print(n)
    if n == 5:
        break
    n += 1
else:
    print('over')

