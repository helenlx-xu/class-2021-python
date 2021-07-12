for i in range(10):
    if i%3 == 0 :
        print(i)

n = 1
while n <= 4:
    print('*' * n)
    n += 1

n = 1
while n <= 5:
    m = 0
    while m < n :
         print('*',end ='')
         m += 1
    n += 1
    print()
'''
*****
****
***
**
*
'''
n = 1
while n <= 5:
    m = 5
    while m > n :
         print('*',end ='')
         m -= 1
    n += 1
    print()


