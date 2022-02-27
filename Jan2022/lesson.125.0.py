n = 1
while n <= 30:

    if n%3 == 0:
        print('---->',n)

    n += 1

print('*'*30)

n = 3
while n <= 30:
    print('====>',n)
    n += 3

print('*'*30)


n = 1
while n <= 30 and n%3 == 0:
    print('********>',n)
    n += 1



n = 1

while n <= 30:
    if n%3 == 0 and n%5 == 0:
        print('------------------>',n)


    n += 1



sum = 0
i = 1
while i <= 20:
    sum += i
    i += 1

print('---->累加和是:',sum)