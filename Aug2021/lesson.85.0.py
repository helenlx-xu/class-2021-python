#def test():
   # print('-----test-----')
    #a()

#def a():
    #print('----------aaaa---------')
    #a()

#a()

def test(i):
    if i == 10:
        print('10')
    else:
        print(i)
        i += 1
        test(i)

test(1)