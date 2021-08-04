#def get_sum(a, b):
#   r = a + b
#  print(r)

#get_sum(2,6,9)
#get_sum(2,6,9,10)

def get_sum(*args):
    #print(args)
    s = 0
    for i in args:
        a += i
    print('和:', s)

get_sum(1, 2)
get_sum(1, 2, 3, 4, 5)
get_sum(1, 2, 3)
get_sum()



ran_list - [23, 45, 12, 44, 78, 39, 29]

*a, b, c = (1, 2, 3, 4,)
print(a)
print(b)
print(c)

a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)

a, b, *c = (1,2,3,4,5,6,7,8)
